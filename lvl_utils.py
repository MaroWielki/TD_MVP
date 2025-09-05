import pygame
from math import floor,sin, cos, atan2, radians, degrees
from random import uniform, randint
from data import turret_init_database, animation_sprites
from gui_tiles import *

class Level:
    def __init__(self,road_map):
        self.waves=[]
        self.road_map=road_map
    def add_wave(self,wave):
        self.waves.append(wave)

class MobWave:
    def __init__(self):
        self.bunches=[]
    def add(self,bunch):
        self.bunches.append(bunch)

class BunchOfMobs:
    def __init__(self,number:int,mob:str):
        self.number=number
        self.mob=mob

class TurretType:
    def __init__(self,name):
        pass

class AnimationSingle:
    def __init__(self,name,kw):
        self.name = name
        self.path = kw['path']
        self.frame_window_width = kw['frame_window_width']
        self.frame_window_height = kw['frame_window_height']
        self.animation_orientation = kw['animation_orientation']
        self.border = kw['border']
        self.anim_fps = kw['anim_fps']
        self.start_x = kw['start_x']
        self.start_y = kw['start_y']
        if "fire_at_frame" in kw.keys():
            self.fire_at_frame=kw['fire_at_frame']
        if "init_rotation" in kw.keys():
            self.init_rotation = kw['init_rotation']
        else:
            self.init_rotation = 0
        self.frames_count = kw['frames_count']
        self.img_per_row_or_col = kw['img_per_row_or_col']
        self.color_key = kw['color_key']


class AnimationData:
    def __init__(self,kw,sprite_name=None):
        self.animationdata={}
        self.name=sprite_name
        for key in kw:
            self.animationdata[key]=AnimationSingle(key,kw[key])

class ExplosionSprite(pygame.sprite.Sprite):
    def __init__(self,anim_data,database,explosion_xy,px_scale_to_xy:tuple,init_anim_speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.init_animation = "HIT"
        self.explosion_xy=explosion_xy
        self.fps_counter=0
        self.animation_frames = {}
        self.fps=database["fps"]
        self.animation_name="HIT"
        self.remove_me=False
        self.px_scale_to_xy=px_scale_to_xy
        self.data=anim_data
        anim_data = self.data.animationdata["HIT"]
        self.animation_frames["HIT"]=cropp_img(anim_data.path,anim_data.frame_window_width,anim_data.frame_window_height,anim_data.border,anim_data.start_x,anim_data.start_y,anim_data.frames_count,anim_data.img_per_row_or_col,anim_data.animation_orientation,anim_data.color_key,self.px_scale_to_xy)
        self.image = None
        self.rect = pygame.rect.Rect(self.explosion_xy[0],self.explosion_xy[1], self.px_scale_to_xy[0],
                                     self.px_scale_to_xy[1])
        self.rect.center = self.explosion_xy

        if init_anim_speed == 0:
            self.anim_fps = self.data.animationdata[self.animation_name].anim_fps
        else:
            self.anim_fps = init_anim_speed

    def update(self):
        self.fps_counter += 1

        if self.anim_fps != 0:

            self.animation_index = floor(self.fps_counter / (self.fps / self.anim_fps))
            if self.animation_index >= len(self.animation_frames[self.animation_name]):
                self.remove_me = True
                self.animation_index = 0
                self.fps_counter = 0
        self.image = self.animation_frames[self.animation_name][self.animation_index].copy()




class TurretSprite(pygame.sprite.Sprite):
    def __init__(self,data :AnimationData,x:int,y:int,fps,fire_at_frame,px_scale_to_xy:tuple,turret_name:str,init_animation="IDLE",init_anim_speed = 0):
        pygame.sprite.Sprite.__init__(self)
        self.animation_frames = {}
        #self.dmg=dmg
        self.db=turret_init_database[turret_name].copy()
        self.px_scale_to_xy = px_scale_to_xy
        self.is_target_available=False
        self.text_upgrade=""
        #self.turret_range = turret_range
        self.init_animation = init_animation
        self.animation_index=0
        self.data=data
        self.fps=fps
        #self.target_type=target_type
        self.bordered = False
        self.fire_at_frame = self.data.animationdata["FIRE"].fire_at_frame
        self.skip_fire=False
        for anim_name in data.animationdata:
            anim_data=self.data.animationdata[anim_name]
            self.animation_frames[anim_name] =cropp_img(anim_data.path,anim_data.frame_window_width,anim_data.frame_window_height,anim_data.border,anim_data.start_x,anim_data.start_y,anim_data.frames_count,anim_data.img_per_row_or_col,anim_data.animation_orientation,anim_data.color_key,self.px_scale_to_xy)
        self.image=None
        self.x=x
        self.y=y
        self.fps_counter=0
        self.last_attack_time = 0

        self.animation_name = init_animation
        self.rect = pygame.rect.Rect(self.x, self.y, self.px_scale_to_xy[0],
                                     self.px_scale_to_xy[1])
        self.rect.center = (self.x, self.y)
        if init_anim_speed==0:
            self.anim_fps=self.data.animationdata[self.animation_name].anim_fps
        else:
            self.anim_fps=init_anim_speed

    def update(self,mobs:pygame.sprite.Group,database):
        self.fps_counter += 1
        self.is_target_available = False
        self.is_target_available=get_target(self.rect.center,self.db["range"],self.db["target_type"],mobs) is not None
        if self.anim_fps != 0:

            self.animation_index = floor(self.fps_counter / (self.fps / self.anim_fps))
            if self.animation_index >= len(self.animation_frames[self.animation_name]):
                self.animation_index = 0
                self.fps_counter = 0
        self.image = self.animation_frames[self.animation_name][self.animation_index].copy()
        #self.rect = pygame.rect.Rect(self.x, self.y, self.data.animationdata[self.animation_name].frame_window_width,self.data.animationdata[self.animation_name].frame_window_height)
        self.rect.center = (self.x,self.y)
        if self.bordered:
            pygame.draw.rect(self.image,"white",(0,0,self.rect.width-1,self.rect.height-1),1)


        if self.is_target_available and self.last_attack_time+self.db["atsp"]<pygame.time.get_ticks():
            self.last_attack_time= pygame.time.get_ticks()
            self.animation_index = 0
            self.fps_counter = 0
            self.animation_name="FIRE"
            self.skip_fire=False
            self.anim_fps = self.data.animationdata[self.animation_name].anim_fps

        if self.animation_name =="FIRE":
            if self.animation_index == self.fire_at_frame and self.skip_fire==False:
                self.fire()
                self.skip_fire=True
            if self.animation_index == len(self.animation_frames[self.animation_name])-1:
                self.animation_name ="IDLE"
                self.animation_index=0
                self.fps_counter = 0
                self.anim_fps=self.data.animationdata[self.animation_name].anim_fps


    def fire(self):
        ev_dic={
            "action": "shoot_projectile",
            "projectile_type": self.db["projectile_type"],
            "start_xy": self.rect.center,
            "projectile_speed": self.db["projectile_speed"],
            "target_xy": (0,0),
            "dmg" : self.db["dmg"],
            "range": self.db["range"],
            "target_type": self.db["target_type"]
        }
        ev = pygame.event.Event(pygame.USEREVENT,ev_dic)
        pygame.event.post(ev)
    def LMB_down(self):
        ev_dic = {
            "action": "select_turret",
            "turret": self
        }
        ev = pygame.event.Event(pygame.USEREVENT, ev_dic)
        pygame.event.post(ev)
    def LMB_up(self):
        pass
    def RMB_down(self):
        pass
    def RMB_up(self):
        pass


class ProjectileSprite(pygame.sprite.Sprite):
    def __init__(self,data :AnimationData,fps:int,x:int,y:int,move_speed:int,dmg:int,projectile_type:str,target_sprite:pygame.sprite.Sprite=None,target_xy=None,init_animation="IDLE",init_anim_speed = 0,rotation=0,px_scale_to_xy:tuple=None):
        pygame.sprite.Sprite.__init__(self)
        self.target_sprite = target_sprite
        self.remove_me = False
        self.dmg=dmg
        self.projectile_type=projectile_type
        self.animation_frames = {}
        self.init_animation = init_animation
        self.animation_index = 0
        self.move_speed = move_speed
        self.data = data
        self.rotation=rotation
        self.target_xy=target_xy
        self.fps = fps
        for anim_name in data.animationdata:
            anim_ratio=self.data.animationdata[anim_name].frame_window_width/self.data.animationdata[anim_name].frame_window_height
            anim_data = self.data.animationdata[anim_name]
            self.animation_frames[anim_name] = cropp_img(anim_data.path, anim_data.frame_window_width,
                                                          anim_data.frame_window_height, anim_data.border,
                                                          anim_data.start_x, anim_data.start_y, anim_data.frames_count,
                                                          anim_data.img_per_row_or_col, anim_data.animation_orientation,
                                                          anim_data.color_key,(floor(px_scale_to_xy[0]*anim_ratio), px_scale_to_xy[1]),anim_data.init_rotation)

        self.x = x
        self.y = y
        self.fps_counter = 0
        self.animation_name = init_animation
        self.image=self.animation_frames[self.animation_name][0]
        self.rect = pygame.rect.Rect(self.x, self.y, self.data.animationdata[self.animation_name].frame_window_width,
                                      self.data.animationdata[self.animation_name].frame_window_height)

        if init_anim_speed == 0:
             self.anim_fps = self.data.animationdata[self.animation_name].anim_fps
        else:
             self.anim_fps = init_anim_speed

    def update(self,**kwargs):

        self.fps_counter += 1
        self.rotation=kwargs.get("rotation",0)

        if self.anim_fps != 0:
            self.animation_index = floor(self.fps_counter / (self.fps / self.anim_fps))
            if self.animation_index >= len(self.animation_frames[self.animation_name]):
                self.animation_index = 0
                self.fps_counter = 0

        if self.target_sprite is not None:
            trgt=self.target_sprite.rect.center
        else:
            trgt=self.target_xy
        if pygame.math.Vector2(self.rect.center).distance_to(pygame.math.Vector2(trgt)) < self.move_speed:
            if self.target_sprite is not None:
                self.target_sprite.hp-=self.dmg
                self.remove_me = True
            else:
                ev_dic = {
                    "action": "create_explosion",
                    "dmg": self.dmg,
                    "radius":50,
                    "projectile_type": self.projectile_type,
                    "explosion_xy":trgt
                }
                ev = pygame.event.Event(pygame.USEREVENT, ev_dic)
                pygame.event.post(ev)
                self.remove_me = True

        self.move(**kwargs)

    def move(self, **kwargs):

        if self.target_xy is not None:
            self.rotation=degrees(atan2(self.rect.center[0] - self.target_xy[0], self.rect.center[1] - self.target_xy[1]))
            self.image = pygame.transform.rotozoom(self.animation_frames[self.animation_name][self.animation_index],self.rotation,1)
            self.x -= self.move_speed * sin(radians(self.rotation))
            self.y -= self.move_speed * cos(radians(self.rotation))
        elif self.target_sprite is not None:
            self.rotation=degrees(atan2(self.rect.center[0] - self.target_sprite.rect.center[0], self.rect.center[1] - self.target_sprite.rect.center[1]))
            self.image = pygame.transform.rotozoom(self.animation_frames[self.animation_name][self.animation_index],self.rotation,1)
            self.x -= self.move_speed * sin(radians(self.rotation))
            self.y -= self.move_speed * cos(radians(self.rotation))
        else:
            self.image =self.animation_frames[self.animation_name][self.animation_index]

        self.rect = self.image.get_rect().move(self.x,self.y)
        #pygame.draw.rect(self.image, "blue", (0,0,self.rect.width,self.rect.height), 1)

class MobPath:
    def __init__(self,start: list, finish: list ,points: list, offset: list = None):
        self.start = start
        self.finish = finish
        self.offset = offset
        self.points = []
        for i in points:
            self.points.append(i)


class MobSprite(pygame.sprite.Sprite):
    def __init__(self,data :AnimationData,fps:int,  x: int,y:int,path = None,move_speed=0,init_animation="IDLE",init_anim_speed=0,path_offset=[0,0],init_hp:int = None):
        pygame.sprite.Sprite.__init__(self)
        if init_hp!= None:
            self.init_hp=init_hp
        else:
            pass

        self.hp = init_hp
        self.move_speed = move_speed
        self.reached_finish=False
        self.path_point_index=0
        self.path = path
        self.bordered = False
        self.path_offset = path_offset
        self.fps_counter=0
        self.anim_fps = init_anim_speed
        self.fps=fps
        self.data=data
        self.animation_frames={}
        self.init_animation = init_animation
        self.animation_name=init_animation
        for anim_name in data.animationdata:
            anim_data=self.data.animationdata[anim_name]
            self.animation_frames[anim_name] = cropp_img(anim_data.path,anim_data.frame_window_width,anim_data.frame_window_height,anim_data.border,anim_data.start_x,anim_data.start_y,anim_data.frames_count,anim_data.img_per_row_or_col,anim_data.animation_orientation,anim_data.color_key)
        self.image=None
        self.x=x
        self.y=y
        self.rect = pygame.rect.Rect(self.x, self.y, self.data.animationdata[self.animation_name].frame_window_width,
                                     self.data.animationdata[self.animation_name].frame_window_height)
        if init_anim_speed==0:
            self.anim_fps=self.data.animationdata[self.animation_name].anim_fps
        else:
            self.anim_fps=init_anim_speed

    def update(self,**kwargs):
        self.move(**kwargs)
        self.fps_counter += 1
        if self.anim_fps!=0:
            self.animation_index = floor(self.fps_counter / (self.fps / self.anim_fps))
            if self.animation_index >= len(self.animation_frames[self.animation_name]):
                self.animation_index = 0
                self.fps_counter = 0
        self.image = self.animation_frames[self.animation_name][self.animation_index].copy()
        self.rect = pygame.rect.Rect(self.x, self.y, self.data.animationdata[self.animation_name].frame_window_width, self.data.animationdata[self.animation_name].frame_window_height)
        if self.hp is not None:
            color="green"
            if self.hp/self.init_hp<0.6: color="orange"
            if self.hp / self.init_hp < 0.3: color = "red"
            pygame.draw.rect(self.image, color, (0, 0, floor(self.rect.width*(self.hp/self.init_hp)),floor(self.rect.height *0.05)))
        if self.bordered:
            pygame.draw.rect(self.image,"white",(0,0,self.rect.width-1,self.rect.height-1),1)

    def move(self,**kwargs):
        x = kwargs.get("x",None)
        dx = kwargs.get("dx", None)
        y = kwargs.get("y", None)
        dy = kwargs.get("dy", None)
        direction = kwargs.get("direction",None)

        if self.path is not None:
            if abs(self.x - (self.path.finish[0]+self.path_offset[0]))<=self.move_speed and abs(self.y - (self.path.finish[1]+self.path_offset[1]))<=self.move_speed:
                self.reached_finish=True
            else:
                if self.x < self.path.points[self.path_point_index][0]+self.path_offset[0]:
                    dx=self.move_speed
                    self.animation_name="WALK_RIGHT"
                if self.x > self.path.points[self.path_point_index][0]+self.path_offset[0]:
                    dx=-self.move_speed
                    self.animation_name="WALK_LEFT"
                if self.y < self.path.points[self.path_point_index][1]+self.path_offset[1]:
                    dy=self.move_speed
                    self.animation_name="WALK_DOWN"
                if self.y > self.path.points[self.path_point_index][1]+self.path_offset[1]:
                    dy=-self.move_speed
                    self.animation_name="WALK_UP"

                if abs(self.x - (self.path.points[self.path_point_index][0]+self.path_offset[0]))<=self.move_speed and abs(self.y - (self.path.points[self.path_point_index][1]+self.path_offset[1]))<=self.move_speed:
                    self.path_point_index+=1

        if x is not None and y is not None:
            self.x = x
            self.y = y
        if dx is not None:
            self.x+=dx
        if dy is not None:
            self.y+=dy
        if direction is not None:
            self.animation_name = direction



def cropp_img(path,frame_window_width,frame_window_height,border,start_x,start_y,frames_count,img_per_row_or_col,animation_orientation,color_key,px_scale_to_xy=None,init_rotation=0):
    pieces = []
    img = pygame.image.load(path)
    img.set_colorkey(color_key)
    frame_index=0
    while frame_index<frames_count:
        if animation_orientation=="horizontal":
            row_index=floor(frame_index/img_per_row_or_col)
            col_index=int(frame_index%img_per_row_or_col)
        if animation_orientation=="vertical":
            col_index = floor(frame_index / img_per_row_or_col)
            row_index = int(frame_index % img_per_row_or_col)
        frame_x = col_index * frame_window_width +border + start_x
        frame_y = row_index * frame_window_height + border + start_y
        if px_scale_to_xy is None:
            pieces.append(pygame.Surface.subsurface(img,frame_x,frame_y,frame_window_width-border,frame_window_height-border))
        else:
            #pieces.append(pygame.transform.scale(pygame.Surface.subsurface(img, frame_x, frame_y, frame_window_width - border,frame_window_height - border), px_scale_to_xy))

            pieces.append(pygame.transform.rotate(pygame.transform.scale(pygame.Surface.subsurface(img, frame_x, frame_y, frame_window_width - border,frame_window_height - border),px_scale_to_xy),init_rotation))


        frame_index+=1
    return pieces

def load_level(road_name:str,road_tiles,database):
    tile_size=database["double_tile_size_xy"]
    road = read_images("img/road/", road_tiles, tile_size, (43, 45, 48))
    map = []
    map_size_tiles_xy = (40, 28)
    for i in range(map_size_tiles_xy[1]):
        map.append([""] * map_size_tiles_xy[0])

    road_map = pygame.image.load("img/Paths/"+road_name)
    road3x3_dictionary = read_road3x3_dictionary("img/Paths/")
    road3x3_dictionary_pixels = read_road3x3_dictionary_pixels("img/Paths/")
    road_map_mapping = read_road_map_mapping("img/Paths/mapping.csv")
    generate_map(map, road_map, road3x3_dictionary_pixels, road_map_mapping, map_size_tiles_xy)


    tmp = database["resolution_in_tiles_percent_xy"][100-database["wave_menu_width_pt"]][0]*database["tile_size_xy"][0]
    #tmp=floor(database["resolution_xy"][0]*(100-database["wave_menu_width_pt"])/100)
    building_allowed_map = generate_build_map((tmp, database["resolution_xy"][0]), tmp, database["resolution_xy"][1], road_map, 32)

    mob_path=generate_mobs_path(road_map,tile_size)

    background = pygame.transform.scale(pygame.image.load("img/bg2.png").convert(),database["resolution_xy"])
    return map,road,building_allowed_map, mob_path,background

def generate_mobs_path(img:pygame.surface.Surface,tile_size:tuple):
    list = []
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            if img.get_at((x, y))[0] in range(1, 254):
                list.append(((x, y), img.get_at((x, y))[0]))

    list.sort(key=sort_fun)
    dic = {}
    offsety=-1  ### NIE WIEM CZEMU
    st = list.pop(0)
    dic["START"] = [st[0][0]*tile_size[0], (st[0][1]+offsety)*tile_size[1]]
    dic["POINTS"] = []
    for pt in list:
        dic["POINTS"].append([pt[0][0]*tile_size[0], (pt[0][1]+offsety)*tile_size[1]])
    dic["FINISH"] = [list[-1][0][0]*tile_size[0], (list[-1][0][1]+offsety)*tile_size[1]]
    return dic

def generate_build_map(menu_x:tuple,width,height,road_map:pygame.surface.Surface,disallowed_distance_from_path:int):

    # TO TRWA BARDZO DLUGO TRZEBA PRZYSPIESZYC

    map2=[[True for y in range(height)] for x in range(width+menu_x[1]-menu_x[0])]
    #map2=[[True for y in range(768)] for x in range(1366)]

    sizex = floor(width/road_map.get_width())
    sizey = floor(height / road_map.get_height())
    menu_x_range = range(menu_x[0],menu_x[1])
    tmp1=0
    tmp2=0

    for x in range(width+menu_x[1]-menu_x[0]):
        for y in range(height):
            if x in menu_x_range:
                map2[x][y]=False

    for xx in range(road_map.get_width()):
        for yy in range(road_map.get_height()):
            if road_map.get_at((xx,yy)) == (0,0,0,255):
                for xxx in range(xx*sizex-disallowed_distance_from_path,xx*sizex+disallowed_distance_from_path):
                    for yyy in range(yy*sizey-disallowed_distance_from_path,yy*sizey+disallowed_distance_from_path):
                        map2[xxx][yyy]=False
                        tmp1+=1

    return map2

def exclude_from_build_map(map,rect:pygame.rect.Rect,include=False):
    for x in range(rect.x,rect.x+rect.width):
        for y in range(rect.y,rect.y+rect.height):
            map[x][y]=include
    return map

def print_road(screen,map2,road,tile_size_xy):
    for x in range(len(map2)):
        for y in range(len(map2[x])):
            if map2[x][y] != "":
                screen.blit(road[map2[x][y]], (tile_size_xy[1] * y, tile_size_xy[0] * x))

def read_images(folder,data,size,color_key):
    pieces ={}
    for key in data.keys():
        pieces[key]=pygame.image.load(folder+data[key])
        pieces[key].set_colorkey(color_key)
        pieces[key]=pygame.transform.scale(pieces[key],size)
        #pieces[key]=pieces[key].set_colorkey(color_key)
    return pieces


def generate_map(map2,road_map_png,road3x3_dictionary_pixels,road_map_mapping,map_size_tiles_xy:tuple):
    for x in range(map_size_tiles_xy[0]-2):
        for y in range(map_size_tiles_xy[1]-2):
            tmp = read_pixels(road_map_png.subsurface(pygame.rect.Rect(x, y, 3, 3)), 3, 3)
            if find_in_road_dic(road3x3_dictionary_pixels, tmp) is not None:
                insert_3x3_to_map(map2, road_map_mapping[find_in_road_dic(road3x3_dictionary_pixels, tmp)], y + 1,
                                  x + 1)
    for x in range(map_size_tiles_xy[0]-2):
        for y in range(map_size_tiles_xy[1]-2):
            tmp = read_pixels(road_map_png.subsurface(pygame.rect.Rect(x, y, 3, 3)), 3, 3)
            if find_in_road_dic(road3x3_dictionary_pixels, tmp) is not None:
                insert_3x3_to_map(map2, road_map_mapping[find_in_road_dic(road3x3_dictionary_pixels, tmp)], y + 1,
                                  x + 1, corners=True)


def read_pixels(surf:pygame.surface,width:int,height:int):
    ret = {}
    for x in range(width):
        for y in range(height):
            if surf.get_at((x,y)) != (255,255,255,255):
                #ret[x,y]=surf.get_at((x,y))
                ret[x, y]=(0,0,0,0)
    return ret

def find_in_road_dic(road_dic,lookie):
    for i in road_dic:
        if lookie == road_dic[i]:
            return i
    return None

def insert_3x3_to_map(where,what,x,y,corners=False):

    xxx = 0
    yyy = 0
    for xx in range(x - 1, x + 2):
        for yy in range(y - 1, y + 2):
            if corners:
                if len(what[xxx][yyy]) == 2 or "X" in what[xxx][yyy]:
                    where[xx][yy] = what[xxx][yyy]
            else:
                where[xx][yy] = what[xxx][yyy]

            yyy+=1
        xxx += 1
        yyy = 0

def read_road3x3_dictionary(path):
    folder="img/Paths/"
    s=["AD.png","SA.png","SAD.png","SD.png","WA.png","WAD.png","WD.png","WS.png","WSA.png","WSAD.png","WSD.png"]
    tmp={}
    for f in s:
        tmp[f[:-4]]=pygame.image.load(folder+f)
    return tmp

def read_road3x3_dictionary_pixels(folder):
    s = ["AD.png", "SA.png", "SAD.png", "SD.png", "WA.png", "WAD.png", "WD.png", "WS.png", "WSA.png", "WSAD.png",
         "WSD.png"]
    tmp = {}
    for f in s:
        tmp[f[:-4]] = read_pixels(pygame.image.load(folder + f),3,3)
    return tmp

def read_road_map_mapping(path):
    road_map_mapping = {}
    lines2 = []
    with open(path, 'r') as file:
        lines=file.readlines()
        for line in lines:
            lines2.append(line.strip())
        for i in range(floor(len(lines2)/4)):
            road_map_mapping[lines2[4*i].split(",")[0]]=[lines2[4*i+1].split(",")[1:4],lines2[4*i+2].split(",")[1:4],lines2[4*i+3].split(",")[1:4]]
    return road_map_mapping

def generate_wave2(database:dict,levels_list:list):
    ret_wave=[]
    level: Level
    wave: MobWave
    bunch: BunchOfMobs
    pygame.time.get_ticks()
    lvl_number=database["current_level"]
    timestart =pygame.time.get_ticks()
    timeend=timestart+10*1000
    wave_number=database["wave_number"]
    level = levels_list[lvl_number]
    wave=level.waves[wave_number-1]

    for bunch in wave.bunches:
        for i in range(bunch.number):
            ret_wave.append((floor(uniform(timestart,timeend)),AnimationData(animation_sprites[bunch.mob],bunch.mob)))


    return ret_wave

def generate_wave(number_of_mobs:int,mob_type,timestart:int,timeend:int,alghoritm="uniform"):
    wave=[]
    for i in range(number_of_mobs):
        wave.append((floor(uniform(timestart,timeend)),mob_type))
    return wave

def sort_sprites(e):
    return e.y

def spawn_mobs(wave_mob,mobs,database,mob_path1_data):
    tmp_time = pygame.time.get_ticks()
    for w_mob in wave_mob:
        if tmp_time >= w_mob[0]:
            pth_off = [randint(-2, 2) * 2, randint(-2, 2) * 2]
            mob_path_1 = MobPath(mob_path1_data["START"], mob_path1_data["FINISH"], mob_path1_data["POINTS"])
            mobs.add(
                MobSprite(w_mob[1], database["fps"], mob_path_1.start[0] + pth_off[0], mob_path_1.start[1] + pth_off[1],
                          mob_path_1, move_speed=mob_database[w_mob[1].name]["speed"], path_offset=pth_off,init_hp=mob_database[w_mob[1].name]["init_hp"]))
    wave_mob = [x for x in wave_mob if x[0] > tmp_time]
    return mobs,wave_mob

def get_target(turret_xy,turret_range: int,target_type: str,group: pygame.sprite.Group):

    hps=[]
    sprites= group.sprites()


    max_distance = 0
    min_distance = 9999
    max_hp = 0
    min_hp = 9999999

    max_distance_index = None
    min_distance_index = None
    max_hp_index = None
    min_hp_index = None
    for i in range(len(sprites)):
        distance = pygame.math.Vector2(turret_xy).distance_to(sprites[i].rect.center)
        if distance < turret_range:
            if distance > max_distance:
                max_distance=distance
                max_distance_index=i
            if distance < min_distance:
                min_distance=distance
                min_distance_index=i
            if sprites[i].hp > max_hp:
                max_hp=sprites[i].hp
                max_hp_index=i
            if sprites[i].hp < min_hp:
                min_hp=sprites[i].hp
                min_hp_index=i
    if max_hp_index is not None:

        if target_type=="furthest":
            return sprites[max_distance_index]
        if target_type=="closest":
            return sprites[min_distance_index]
        if target_type=="most_hp":
            return sprites[max_hp_index]
        if target_type=="least_hp":
            return sprites[min_hp_index]

    return None

def sort_fun(a:list):
    return a[1]

def deal_splash_dmg(explosion_xy,dmg,radius,mobs_sprite_list:pygame.sprite.Group):
    for mob in mobs_sprite_list:
        dist=pygame.Vector2(mob.rect.center).distance_to(pygame.Vector2(explosion_xy))
        if dist <radius:
            mob.hp-=floor(dmg*(1-(dist/radius)))

def update_shop_details(menu,database):

    database["food_change"]=0
    database["gems_change"] = 0

    for active in menu["LevelMenu/Title0/Title0/gridActive"].members_group:
        database["food_change"]-=active.data["food_cost"]
        database["gems_change"] -= active.data["gems_cost"]
    menu["LevelMenu/Title0/Title2/TextFood"].update(txt="Food: " + str(database["food"]))
    menu["LevelMenu/Title0/Title2/TextGems"].update(txt="Gems: " + str(database["gems"]))
    if database["food_change"] !=0:
        menu["LevelMenu/Title0/Title2/TextFood_change"].update(txt=str(database["food_change"]))
    else:
        menu["LevelMenu/Title0/Title2/TextFood_change"].update(txt="")
    if database["gems_change"] !=0:
        menu["LevelMenu/Title0/Title2/TextGems_change"].update(txt=str(database["gems_change"]))
    else:
        menu["LevelMenu/Title0/Title2/TextGems_change"].update(txt="")

    if -database["gems_change"] >database["gems"] or -database["food_change"] >database["food"] or len(menu["LevelMenu/Title0/Title0/gridActive"].members_group)<1:
        for index in range(1,7):
            menu['LevelMenu/Title'+str(index)+'/buttonStartLvl'+str(index)].is_active=False
    else:
        for index in range(1, 7):
            menu['LevelMenu/Title' + str(index) + '/buttonStartLvl' + str(index)].is_active = True

def update_shop_mm_details(menu,database):

    #menu["LevelMenu/Title0/Title2/TextFood"].update(txt="Food: " + str(database["food"]))
    menu["ShopMenu/Title1/TextGems"].update(txt=str(database["gems"]))


    if database["gems_change"] !=0:
        menu["ShopMenu/Title1/TextGems_change"].update(txt=str(database["gems_change"]))
    else:
        menu["ShopMenu/Title1/TextGems_change"].update(txt="")

    if -database["gems_change"] >database["gems"] :
        for index in range(1,3):
            menu['ShopMenu/button'+str(index)].is_active=False
    else:
        for index in range(1, 3):
            menu['ShopMenu/button'+str(index)].is_active=True

    # if -database["gems_change"] >database["gems"] or -database["food_change"] >database["food"]:
    #     for index in range(1,7):
    #         menu['LevelMenu/Title'+str(index)+'/buttonStartLvl'+str(index)].is_active=False
    # else:
    #     for index in range(1, 7):
    #         menu['LevelMenu/Title' + str(index) + '/buttonStartLvl' + str(index)].is_active = True

def update_armory_mm_details(menu,database):

    #menu["LevelMenu/Title0/Title2/TextFood"].update(txt="Food: " + str(database["food"]))
    menu["ArmoryMenu/Title1/TextGems"].update(txt=str(database["gems"]))

    for index_1 in range(len(database["available_turrets"])):
        for what in ["dmg", "atsp", "range"]:
            if what == "dmg": what_1 = "DMG"
            if what == "atsp": what_1 = "ATSP"
            if what == "range": what_1 = "Range"
            menu["ArmoryMenu/grid" + str(index_1) + "/Text" + what_1 + ""].update(txt=what_1+": "+str(turret_init_database[database["available_turrets"][index_1]][what]))


    if database["gems_change"] !=0:
        menu["ArmoryMenu/Title1/TextGems_change"].update(txt=str(database["gems_change"]))
    else:
        menu["ArmoryMenu/Title1/TextGems_change"].update(txt="")

    if database["armory_change"] != ():
        if database["armory_change"][1] == "dmg": what = "DMG"
        if database["armory_change"][1] == "atsp": what = "ATSP"
        if database["armory_change"][1] == "range": what = "Range"
        text_change_name = "ArmoryMenu/grid" + str(database["armory_change"][0]) + "/Text" + what + "_change"

        menu[text_change_name].update(txt=str(database["armory_change"][2]))
    else:
        for index_1 in range(len(database["available_turrets"])):
            for what in ["DMG","ATSP","Range"]:
                menu["ArmoryMenu/grid" + str(index_1) + "/Text" + what + "_change"].update(txt="")

    if -database["gems_change"] >database["gems"] :
        for index in range(len(database["available_turrets"])):
            menu['ArmoryMenu/grid' + str(index) +"ButtonATSP"].is_active=False
            menu['ArmoryMenu/grid' + str(index) + "ButtonDMG"].is_active = False
            menu['ArmoryMenu/grid' + str(index) + "ButtonRange"].is_active = False
    else:
        for index in range(len(database["available_turrets"])):
            menu['ArmoryMenu/grid' + str(index) + "ButtonATSP"].is_active = True
            menu['ArmoryMenu/grid' + str(index) + "ButtonDMG"].is_active = True
            menu['ArmoryMenu/grid' + str(index) + "ButtonRange"].is_active = True

    # if -database["gems_change"] >database["gems"] or -database["food_change"] >database["food"]:
    #     for index in range(1,7):
    #         menu['LevelMenu/Title'+str(index)+'/buttonStartLvl'+str(index)].is_active=False
    # else:
    #     for index in range(1, 7):
    #         menu['LevelMenu/Title' + str(index) + '/buttonStartLvl' + str(index)].is_active = True

def grand_prices(database,prices):
    for price in prices:
        if price=="chicken":
            database["food"]+=1
        if price=="steak":
            database["food"]+=3
        if price=="gem":
            database["gems"]+=1
        if price=="catapult":
            database["available_turrets"].append(price)
        if price=="archer":
            database["available_turrets"].append(price)
        if price=="cyclop":
            database["available_turrets"].append(price)




def subtract_costs(database,costs):
    database["food"]+=database["food_change"]
    database["gems"] += database["gems_change"]
    # for active in costs.members_group:
    #     database["food_change"] -= active.data["food_cost"]
    #     database["gems_change"] -= active.data["gems_cost"]