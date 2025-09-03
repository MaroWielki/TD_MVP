


from sys import exit
import asyncio
import pygame.sprite
from pygame import K_ESCAPE


import pygame

available_turrets=["archer","catapult","cyclop"]
available_enemies=["goblin","spider","skeleton"]
available_bosses=["eye"]
available_bosses_price=["victory"]
available_prices=["chicken","steak","gem","random_turret"]
#available_prices=["chicken","steak","gem","random_turret","random_item"]


mob_database={
    "goblin_sprite":{
        "init_hp":100,
        "speed":1,
        "award": 10
    },
    "skeleton_sprite":{
        "init_hp":75,
        "speed":2,
        "award": 15
    },
    "spider_sprite":{
        "init_hp":25,
        "speed":3,
        "award": 5
    },
    "eye_sprite":{
        "init_hp":500,
        "speed":1,
        "award": 30
    },
}

item_data={
    "random_turret":{
        "size":(1,1),
        "scale": 1,
        "sprite": "random_turret_sprite"
    },
    "victory": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "victory_sprite"
    },
    "random_item": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "random_item_sprite"
    },
    "eye": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "eye_sprite"
    },
    "shirt":{
        "size":(2,2),
        "scale":2
    },
    "gem":{
        "size":(1,1),
        "scale": 1,
        "sprite": "gem_sprite"
    },
    "chicken": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "chicken_sprite"
    },
    "steak": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "steak_sprite"
    },
    "goblin": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "goblin_sprite"
    },
    "spider": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "spider_sprite"
    },
    "skeleton": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "skeleton_sprite"
    },


    "catapult":{
        "size":(1,1),
        "scale":1,
        "sprite":"catapult_sprite",
        "cost": 100,
        "food_cost":3,
"gems_cost":0,
        "name":"catapult"
    },
    "archer": {
        "size": (1, 1),
        "scale": 1,
        "sprite":"archer_sprite",
        "cost": 50,
"food_cost":2,
"gems_cost":0,
        "name":"archer"
    },
    "cyclop": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "cyclop_sprite",
        "cost": 100,
"food_cost":2,
        "gems_cost":0,
        "name": "cyclop"
    }

}



class Item:
    def __init__(self, tile_size_xy:tuple,name):
        self.name=name
        self.data=item_data[name]
        self.image=pygame.transform.scale(pygame.image.load("img/items/"+name+".png"),(tile_size_xy[0]*self.data["scale"],tile_size_xy[1]*self.data["scale"]))



class GuiTiles1:
    def __init__(self,tile_size):
        folder="img/GUI/1 Interface/"
        self.WA=pygame.transform.scale(pygame.image.load(folder + "Tile_01.png"),tile_size)
        self.W=pygame.transform.scale(pygame.image.load(folder + "Tile_02.png"),tile_size)
        self.WD = pygame.transform.scale(pygame.image.load(folder + "Tile_03.png"),tile_size)

        self.A=pygame.transform.scale(pygame.image.load(folder + "Tile_13.png"),tile_size)
        self.M=pygame.transform.scale(pygame.image.load(folder + "Tile_14.png"),tile_size)
        self.D=pygame.transform.scale(pygame.image.load(folder + "Tile_15.png"),tile_size)

        self.SA=pygame.transform.scale(pygame.image.load(folder + "Tile_25.png"),tile_size)
        self.S=pygame.transform.scale(pygame.image.load(folder + "Tile_26.png"),tile_size)
        self.SD=pygame.transform.scale(pygame.image.load(folder + "Tile_27.png"),tile_size)
        self.width=self.WA.get_width()
        self.height=self.WA.get_height()

class GuiCheckBoxTile:
    def __init__(self,tile_size):
        folder = "img/road/"

        im=pygame.image.load(folder + "checkbox_13.png")

        #self.Unchecked = pygame.transform.smoothscale(pygame.image.load(folder + "Tile_93.png").convert(), tile_size)
        self.Unchecked = pygame.transform.scale(pygame.image.load(folder + "checkbox_13.png").convert(), tile_size)
        #self.Unchecked = pygame.transform.scale(pygame.image.load(folder + "Tile_93.png"), tile_size)
        cross = pygame.image.load("img/GUI/3 Icons/Iconset7.png")
        cross=cross.subsurface((91,1,8,8))
        cross = pygame.transform.scale(cross, tile_size)
        self.Checked=self.Unchecked.copy()
        self.Checked.blit(cross, (0,0))

        self.width=self.Unchecked.get_width()
        self.height=self.Unchecked.get_height()

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

    if -database["gems_change"] >database["gems"] or -database["food_change"] >database["food"]:
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

from gui_tiles import item_data
from lvl_utils import *

# levels_list={}
#
# wave0=MobWave()
# wave0.add(BunchOfMobs(6,"spider_sprite"))
# wave1=MobWave()
# wave1.add(BunchOfMobs(6,"goblin_sprite"))
# wave2=MobWave()
# wave2.add(BunchOfMobs(12,"goblin_sprite"))
# wave3=MobWave()
# wave3.add(BunchOfMobs(24,"goblin_sprite"))
# wave4=MobWave()
# wave4.add(BunchOfMobs(48,"goblin_sprite"))
# wave5=MobWave()
# wave5.add(BunchOfMobs(6,"skeleton_sprite"))
#
#
# levels_list[1]=Level("umapc")
# levels_list[1].add_wave(wave0)
# levels_list[1].add_wave(wave5)
#
# levels_list[2]=Level("zigzagc")
# levels_list[2].add_wave(wave1)
# levels_list[2].add_wave(wave2)
# levels_list[2].add_wave(wave3)
#
# levels_list[3]=Level("bulb")
# levels_list[3].add_wave(wave1)
# levels_list[3].add_wave(wave2)
# levels_list[3].add_wave(wave3)
#
#
# levels_list[4]=Level("cos")
# levels_list[4].add_wave(wave1)
# levels_list[4].add_wave(wave2)
# levels_list[4].add_wave(wave3)
# levels_list[4].add_wave(wave4)
#
# levels_list[5]=Level("zmap")
# levels_list[5].add_wave(wave1)
# levels_list[5].add_wave(wave2)
# levels_list[5].add_wave(wave3)
# levels_list[5].add_wave(wave4)
#
# levels_list[6]=Level("long")
# levels_list[6].add_wave(wave1)
# levels_list[6].add_wave(wave2)
# levels_list[6].add_wave(wave3)
# levels_list[6].add_wave(wave4)

def wave_generator(input):
    levels_list={}

    wave0 = MobWave()
    wave0.add(BunchOfMobs(6, "spider_sprite"))

    levels_list[1] = Level("umapc")
    levels_list[2] = Level("zigzagc")
    levels_list[3] = Level("bulb")
    levels_list[4] = Level("cos")
    levels_list[5] = Level("zmap")
    levels_list[6] = Level("long")

    mobs_in_bunch = {"spider": 12, "skeleton": 4, "goblin": 5, "eye": 2}
    waves_in_lvl = {1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8}
    bunches_in_wave = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 4,7:7,8:8}


    for lvl_index in range(1,7):
        for wave_index in range(waves_in_lvl[lvl_index]):
            wave=MobWave()
            for bunch_index in range(bunches_in_wave[wave_index+1]):
                mob=input[lvl_index-1][randint(0,len(input[lvl_index-1])-1)]
                wave.add(BunchOfMobs(mobs_in_bunch[mob],item_data[mob]["sprite"]))
            levels_list[lvl_index].add_wave(wave)


        # for mob in input[index]:
        #     wave = MobWave()
        #     wave.add(BunchOfMobs(12,item_data[mob]["sprite"]))
        #     levels_list[index+1].add_wave(wave)

    return levels_list

#from create_menus import *


def get_xy(menu_start_xy:tuple,tile_size_xy:tuple, x_index:int,y_index:int):
    return menu_start_xy[0]+x_index*tile_size_xy[0],menu_start_xy[1]+y_index*tile_size_xy[1]

def get_xy_for_centralized(bigger:tuple,smaller:tuple):
    x=floor(bigger[0]/2)-floor(smaller[0]/2)
    y = floor(bigger[1] / 2) - floor(smaller[1] / 2)
    return x,y


def get_member_by_name(sprites_list:list,name:str):
    for spr in sprites_list:
        if spr.name == name:
            return spr
    return None

def get_fonts_sizes(font_list:list,sizes:list):
    ret={}
    for fnt in font_list:
        siz={}
        for size in sizes:
            font = pygame.font.SysFont(fnt, size)
            siz[size]=font.get_height()
        ret[fnt]=siz
    return ret

def get_font_size_no_bigger_then(fnt:str,px_height:int,fnt_sizes:dict):
    ret=0
    tmp=0
    for i in fnt_sizes[fnt]:
        if fnt_sizes[fnt][i]<=px_height and fnt_sizes[fnt][i]>tmp:
            tmp=fnt_sizes[fnt][i]
            ret=i
    return ret

def cropp_img2(path,frame_size_xy:tuple,start_xy,frames_count,row_step, col_step,img_per_row_or_col,color_key,frame_size_scaleto_xy:tuple=None):
    pieces = []
    img = pygame.image.load(path)
    img.set_colorkey(color_key)
    frame_index=0
    while frame_index<frames_count:
        row_index = floor(frame_index / img_per_row_or_col)
        col_index = int(frame_index % img_per_row_or_col)
        frame_x = start_xy[0] + col_index*(row_step+frame_size_xy[0])
        frame_y =  start_xy[1] + row_index*(col_step+frame_size_xy[1])


        if frame_size_scaleto_xy is None:
            pieces.append(pygame.Surface.subsurface(img,frame_x,frame_y,frame_size_xy[0],frame_size_xy[1]))
        else:
            pieces.append(pygame.transform.scale(pygame.Surface.subsurface(img,frame_x,frame_y,frame_size_xy[0],frame_size_xy[1]),frame_size_scaleto_xy))
        frame_index+=1
    return pieces



class MenuTitle(pygame.sprite.Sprite):
    def __init__(self,px_parent_xy:tuple,database:dict,start_in_tiles_xy,size_in_tiles_xy:tuple,name:str,title="",tile_size_xy=None,draggable=True,background=""):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.draggable = draggable
        self.anchor_to_mouse=False
        self.size_in_tiles_xy=size_in_tiles_xy
        self.start_in_tiles_xy=start_in_tiles_xy
        if tile_size_xy is None:
            self.tile_size_xy=database["tile_size_xy"]
        else:
            self.tile_size_xy=tile_size_xy

        self.members_group = pygame.sprite.Group()
        self.title=title
        self.px_start_xy=get_xy(px_parent_xy,self.tile_size_xy,start_in_tiles_xy[0],start_in_tiles_xy[1])
        self.px_size_xy = (size_in_tiles_xy[0]*self.tile_size_xy[0],size_in_tiles_xy[1]*self.tile_size_xy[1])
        self.image=pygame.Surface((self.px_size_xy[0],self.px_size_xy[1]))
        self.image.set_colorkey((0,0,0))
        self.rect=pygame.rect.Rect(self.px_start_xy[0],self.px_start_xy[1],self.px_size_xy[0],self.px_size_xy[1])

        self.gui_tiles = GuiTiles1(self.tile_size_xy)



        ##HEAD
        self.image.blit(self.gui_tiles.WA,(0,0))
        for i in range(self.size_in_tiles_xy[0]-2):
            self.image.blit(self.gui_tiles.W, ((i+1)*self.tile_size_xy[0], 0))
        self.image.blit(self.gui_tiles.WD, ((self.size_in_tiles_xy[0]-1)*self.tile_size_xy[0], 0))

        ## MID
        for j in range(self.size_in_tiles_xy[1]-2):
            self.image.blit(self.gui_tiles.A, (0, (j+1)*self.tile_size_xy[1]))
            for i in range(self.size_in_tiles_xy[0] - 2):
                self.image.blit(self.gui_tiles.M, ((i + 1) * self.tile_size_xy[0], (j+1)*self.tile_size_xy[1]))
            self.image.blit(self.gui_tiles.D, ((self.size_in_tiles_xy[0] - 1) * self.tile_size_xy[0], (j+1)*self.tile_size_xy[1]))

        ## BOTTOM
        self.image.blit(self.gui_tiles.SA, (0, (self.size_in_tiles_xy[1]-1)*self.tile_size_xy[1]))
        for i in range(self.size_in_tiles_xy[0] - 2):
            self.image.blit(self.gui_tiles.S, ((i + 1) * self.tile_size_xy[0], (self.size_in_tiles_xy[1]-1)*self.tile_size_xy[1]))
        self.image.blit(self.gui_tiles.SD, ((self.size_in_tiles_xy[0] - 1) * self.tile_size_xy[0], (self.size_in_tiles_xy[1]-1)*self.tile_size_xy[1]))
        ###
        fnt_size=get_font_size_no_bigger_then("comicsansms",floor(tile_size_xy[1]*0.8),database["font_sizes"])
        font = pygame.font.SysFont("comicsansms", fnt_size)
        header_text = font.render(self.title, True, 'BLUE')

        xy_for_header=get_xy_for_centralized((self.size_in_tiles_xy[0]*self.tile_size_xy[0], self.tile_size_xy[1]),(header_text.get_width(),header_text.get_height()))
        self.image.blit(header_text,xy_for_header)

        if background!="":
            background_image=pygame.image.load(background)
            background_image.set_colorkey((12,32,12))
            background_image=pygame.transform.scale(background_image,(self.rect.size[0]-tile_size_xy[0],self.rect.size[1]-floor(2.5*tile_size_xy[1])))
            self.image.blit(background_image,(floor(tile_size_xy[0]/2),tile_size_xy[1]))

    def update(self,**kwargs):
        #pygame.draw.rect(self.image,"yellow",pygame.rect.Rect(0,0,self.px_size_xy[0],self.px_size_xy[1]),1)

        new_px_parent_xy=kwargs.get("px_parent_xy",None)

        if self.anchor_to_mouse:

            new_px_parent_xy=(pygame.mouse.get_pos()[0] - self.px_anchor_xy[0],pygame.mouse.get_pos()[1] - self.px_anchor_xy[1])


        if new_px_parent_xy is not None:
            self.px_parent_xy=new_px_parent_xy

            self.px_start_xy = get_xy(self.px_parent_xy, self.tile_size_xy, self.start_in_tiles_xy[0], self.start_in_tiles_xy[1])

            self.px_size_xy = (self.size_in_tiles_xy[0] * self.tile_size_xy[0], self.size_in_tiles_xy[1] * self.tile_size_xy[1])
            self.rect = pygame.rect.Rect(self.px_start_xy[0], self.px_start_xy[1], self.px_size_xy[0],
                                         self.px_size_xy[1])


        self.members_group.update(px_parent_xy=self.px_start_xy,allowed_map=kwargs.get("allowed_map",None))

        # if self.anchor_to_mouse:
        #     self.update(px_parent_xy=(pygame.mouse.get_pos()[0] - self.px_anchor_xy[0],
        #                               pygame.mouse.get_pos()[1] - self.px_anchor_xy[1]))


    def draw(self,surface):
        #self.members_group.draw(surface)
        surface.blit(self.image,self.rect)
        for mm in self.members_group.sprites(): mm.draw(surface)

    def add(self,sprite:pygame.sprite.Sprite):
        self.members_group.add(sprite)
        return get_member_by_name(self.members_group.sprites(),sprite.name)

    def remove(self,sprite:pygame.sprite.Sprite):
        sprite.remove(self.members_group)

    def hoover(self,**kwargs):
        pass

    def LMB_down(self):

        if self.draggable and pygame.rect.Rect(self.px_start_xy[0],self.px_start_xy[1],self.px_size_xy[0],self.tile_size_xy[1]).collidepoint(pygame.mouse.get_pos()):

            self.anchor_to_mouse=True
            self.px_anchor_xy=(pygame.mouse.get_pos()[0]-self.px_start_xy[0],pygame.mouse.get_pos()[1]-self.px_start_xy[1])


    def LMB_up(self):
        self.anchor_to_mouse=False

    def RMB_down(self):
        pass
    def RMB_up(self):
        pass

class GuiCheckbox(pygame.sprite.Sprite):
    def __init__(self,px_parent_xy:tuple,start_in_tiles_xy:tuple,tile_size_xy:tuple,name:str,text:str,size,parent_object,ticked=False,):
        pygame.sprite.Sprite.__init__(self)
        self.gui_tiles = GuiCheckBoxTile(size)
        self.text = text
        self.name=name
        self.parent_object=parent_object
        self.space=10
        self.tile_size_xy=tile_size_xy
        self.start_in_tiles_xy=start_in_tiles_xy
        self.px_parent_xy=px_parent_xy
        font = pygame.font.SysFont("comicsansms", 12)
        checkbox_text = font.render(self.text, True, 'BLUE')

        self.img_unchecked = pygame.Surface((checkbox_text.get_width()+size[0]+self.space,max(checkbox_text.get_height(),self.gui_tiles.height)),pygame.SRCALPHA)
        #pygame.draw.rect(surf,"white",surf.get_rect())

        xy_for_checkbox=get_xy_for_centralized((self.img_unchecked.get_width(),self.img_unchecked.get_height()),(self.gui_tiles.width,self.gui_tiles.height))

        self.img_checked=self.img_unchecked.copy()
        self.img_unchecked.blit(self.gui_tiles.Unchecked,(0,xy_for_checkbox[1]))
        self.img_checked.blit(self.gui_tiles.Checked, (0, xy_for_checkbox[1]))
        xy_for_text = get_xy_for_centralized((self.img_unchecked.get_width(),self.img_unchecked.get_height()),(checkbox_text.get_width(),checkbox_text.get_height()))
        self.img_checked.blit(checkbox_text,(xy_for_text[0]+self.space,xy_for_text[1]))
        self.img_unchecked.blit(checkbox_text,(xy_for_text[0]+self.space,xy_for_text[1]))
        self.image=self.img_unchecked
        self.rect=self.image.get_rect()

    def update(self,**kwargs):

        if self.parent_object.db["target_type"]==self.text:
            self.image=self.img_checked
        else:
            self.image = self.img_unchecked

        # if turret_database is not None and self.text == turret_database["TARGET_TYPE"]:
        #     self.image=self.img_checked
        # else:
        #     self.image=self.img_unchecked

        #if kwargs.get("txt", None) is not None:
        #    self.image= self.font.render(kwargs.get("txt"), True, "yellow")
        new_px_parent_xy = kwargs.get("px_parent_xy", None)
        if new_px_parent_xy is not None:
            self.px_parent_xy = new_px_parent_xy
            self.rect = self.image.get_rect().move(
                get_xy(self.px_parent_xy, self.tile_size_xy, self.start_in_tiles_xy[0], self.start_in_tiles_xy[1]))

    def hoover(self, **kwargs):
        pass
    def draw(self,surface):
        #self.members_group.draw(surface)
        surface.blit(self.image,self.rect)
    def LMB_down(self):
        self.parent_object.db["target_type"]=self.text
    def LMB_up(self):
        pass
    def RMB_down(self):
        pass
    def RMB_up(self):
        pass


class ItemMenu(pygame.sprite.Sprite):
    def __init__(self,px_parent_xy:tuple,database:dict,start_in_tiles_xy,name:str,item_name:str,parent_grid,tile_size_xy:tuple=None,draggable=True):
        pygame.sprite.Sprite.__init__(self)
        if tile_size_xy is None:
            self.tile_size_xy=database["tile_size_xy"]
        else:
            self.tile_size_xy=tile_size_xy
        self.legal_to_place=True
        self.name=name
        self.draggable=draggable
        self.item_name=item_name
        self.build_or_place=""
        self.new_px_parent_xy=None
        self.parent_grid=parent_grid
        self.parent_grid_pickup=parent_grid
        self.parent_grid_pickup_xy=start_in_tiles_xy
        self.item = Item(self.tile_size_xy, item_name)
        self.img = self.item.image.copy()
        self.image = self.img
        self.img_gray = pygame.transform.grayscale(self.item.image)
        self.data = self.item.data
        self.size_in_tiles_xy = self.data["size"]
        self.px_parent_xy=px_parent_xy
        self.start_in_tiles_xy=start_in_tiles_xy
        self.occupy_grid_start_in_tiles_xy=self.start_in_tiles_xy
        self.is_pressed=False
        self.is_hoovered = False
        self.anchor_to_mouse=False
        self.px_start_xy=get_xy(px_parent_xy,self.tile_size_xy,start_in_tiles_xy[0],start_in_tiles_xy[1])
        self.px_size_xy = (self.size_in_tiles_xy[0]*self.tile_size_xy[0],self.size_in_tiles_xy[1]*self.tile_size_xy[1])

        self.rect=self.image.get_rect().move(self.px_start_xy[0],self.px_start_xy[1])

        pygame.draw.rect(self.image,"white",(0,0,self.rect.size[0],self.rect.size[1]),1)

    def update(self,**kwargs):

        ### Movement and allowed_map
        self.new_px_parent_xy = kwargs.get("px_parent_xy", None)
        allowed_map = kwargs.get("allowed_map", None)
        mouse_pos = pygame.mouse.get_pos()
        if allowed_map != {}:
            try:
                if allowed_map[self.rect.topleft[0]][ self.rect.topleft[1]]== False or allowed_map[self.rect.topright[0]][ self.rect.topright[1]] == False or allowed_map[self.rect.bottomleft[0]][ self.rect.bottomleft[1]] == False or allowed_map[self.rect.bottomright[0]][ self.rect.bottomright[1]] == False:
                    ### TU TRZEBA SPRAWDZIC 4 NAROZNIKI ALBO CONIDERA JAKIEGOS KURWA NIE WIEM
                    self.legal_to_place = False
                else:
                    self.legal_to_place = True
                    self.build_or_place_on_grid="build"
            except KeyError:
                self.legal_to_place = False
            except IndexError:
                self.legal_to_place = False


        if self.anchor_to_mouse:

            #self.new_px_parent_xy = (pygame.mouse.get_pos()[0] - self.px_anchor_xy[0],pygame.mouse.get_pos()[1] - self.px_anchor_xy[1])
            self.rect.center=pygame.mouse.get_pos()
            self.new_px_parent_xy=self.rect.topleft


        if self.new_px_parent_xy is not None:
            self.px_parent_xy = self.new_px_parent_xy
            if self.anchor_to_mouse:
                self.px_start_xy = self.new_px_parent_xy
            else:
                self.px_start_xy = get_xy(self.px_parent_xy, self.tile_size_xy, self.start_in_tiles_xy[0],
                                          self.start_in_tiles_xy[1])
            self.px_size_xy = (self.size_in_tiles_xy[0] * self.tile_size_xy[0],
                               self.size_in_tiles_xy[1] * self.tile_size_xy[1])
            self.rect = pygame.rect.Rect(self.px_start_xy[0], self.px_start_xy[1], self.px_size_xy[0],
                                         self.px_size_xy[1])

        # OCCUPY GRID
        self.occupy_grid_start_in_tiles_xy = get_xy_index_from_px(self.px_start_xy,
                                                                  self.parent_grid.start_in_tiles_xy,
                                                                  self.parent_grid.px_parent_xy,
                                                                  self.parent_grid.tile_size_xy)

        #self.legal_to_place=True
        if self.occupy_grid_start_in_tiles_xy[0]<0 or self.occupy_grid_start_in_tiles_xy[1]<0:
            pass
            #self.legal_to_place = False
        tmp=False
        for x in range(self.data["size"][0]):
            for y in range(self.data["size"][1]):

                if self.draggable and self.occupy_grid_start_in_tiles_xy[0]+x<self.parent_grid.size_in_tiles_xy[0] and self.occupy_grid_start_in_tiles_xy[1]+y<self.parent_grid.size_in_tiles_xy[1]:
                    if self.occupy_grid_start_in_tiles_xy[0]+x>=0 and self.occupy_grid_start_in_tiles_xy[1]+y >=0:
                        self.parent_grid.occupied_xy[self.occupy_grid_start_in_tiles_xy[0]+x][self.occupy_grid_start_in_tiles_xy[1]+y]=True
                        tmp=True
                else:
                    pass
        if tmp==True:
            self.legal_to_place=True
            self.build_or_place_on_grid = "place"



        if self.legal_to_place or self.draggable==False:
            self.image = self.img
        else:
            self.image = self.img_gray





        self.new_px_parent_xy=None


    def draw(self,surface):
        #self.members_group.draw(surface)
        surface.blit(self.image,self.rect)

    def hoover(self, **kwargs):
        pass

    def LMB_down(self):
        ## Put item
        if self.anchor_to_mouse:
            if self.legal_to_place:
                if self.build_or_place_on_grid=="place":
                    if self.parent_grid!= self.parent_grid_pickup: sent_action_event(action="move_item_from_grid_to_grid",item=self,old_grid=self.parent_grid_pickup,new_grid=self.parent_grid,new_grid_start_in_tiles_xy=self.occupy_grid_start_in_tiles_xy,tile_size_xy=self.tile_size_xy)
                    self.anchor_to_mouse=False
                    self.image = self.item.image.copy()
                    self.px_anchor_xy=None
                    self.start_in_tiles_xy=(self.occupy_grid_start_in_tiles_xy)

                if self.build_or_place_on_grid == "build":
                    self.anchor_to_mouse = False
                    self.image = self.item.image.copy()
                    self.start_in_tiles_xy = self.parent_grid_pickup_xy
                    sent_action_event(action="build_turret",turret=self)


        ## Pickup item
        else:
        #else:
            ### po co to sprawdzenie??

            if self.draggable and  pygame.rect.Rect(self.px_start_xy[0], self.px_start_xy[1], self.px_size_xy[0],
                                                    self.px_size_xy[1]).collidepoint(pygame.mouse.get_pos()):
                self.anchor_to_mouse = True
                #drag by point where clicked

                self.px_anchor_xy = (pygame.mouse.get_pos()[0] - self.px_start_xy[0],pygame.mouse.get_pos()[1] - self.px_start_xy[1])

                #self.px_anchor_xy = (self.rect.center)

                self.parent_grid_pickup=self.parent_grid
                self.parent_grid_pickup_xy=self.occupy_grid_start_in_tiles_xy


    def LMB_up(self):
        pass
    def RMB_down(self):

        self.anchor_to_mouse=False
        self.image = self.item.image.copy()
        self.start_in_tiles_xy=self.parent_grid_pickup_xy

    def RMB_up(self):
        pass


class MenuText(pygame.sprite.Sprite):
    def __init__(self,px_parent_xy:tuple,database:dict,start_in_tiles_xy,name:str,txt:str,tile_size_xy:tuple=None,parent_object=None,variable_name:str=None):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.parent_object = parent_object
        self.variable_name = variable_name
        self.start_in_tiles_xy=start_in_tiles_xy
        self.px_parent_xy=px_parent_xy
        if tile_size_xy is None:
            self.tile_size_xy=database["tile_size_xy"]
        else:
            self.tile_size_xy=tile_size_xy
        self.txt=txt
        self.font = pygame.font.SysFont("comicsansms", 16)
        self.image = self.font.render(txt, True, "yellow")
        self.rect = self.image.get_rect().move(get_xy(px_parent_xy, self.tile_size_xy, self.start_in_tiles_xy[0], start_in_tiles_xy[1]))

    def update(self,**kwargs):
        # datbase=kwargs.get("database")
        # if datbase is not None:
        #     if self.variable_name =="food_change":
        #         self.image = self.font.render(datbase["food_change"], True, "yellow")
        #     if self.variable_name =="gems_change":
        #         self.image = self.font.render(datbase["gems_change"], True, "yellow")

        if kwargs.get("txt", None) is not None:
            self.image= self.font.render(kwargs.get("txt"), True, "yellow")

        if self.parent_object is not None and self.variable_name is not None:
            self.image = self.font.render(str(self.parent_object.db[self.variable_name]), True, "yellow")
            if self.variable_name[-7:]=="_change": self.parent_object.db[self.variable_name]=""




        new_px_parent_xy = kwargs.get("px_parent_xy", None)
        if new_px_parent_xy is not None:
            self.px_parent_xy = new_px_parent_xy
            self.rect = self.image.get_rect().move(
                get_xy(self.px_parent_xy, self.tile_size_xy, self.start_in_tiles_xy[0], self.start_in_tiles_xy[1]))

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def hoover(self,**kwargs):
        pass

    def LMB_down(self):
        pass
    def LMB_up(self):
        pass
    def RMB_down(self):
        pass
    def RMB_up(self):
        pass


# class MenuCheckbox(pygame.sprite.Sprite):
#     def __init__(self,px_parent_xy:tuple,database:dict,start_in_tiles_xy,name:str,text:str,tile_size_xy:tuple=None,checked=False):
#         pygame.sprite.Sprite.__init__(self)
#         if tile_size_xy is None:
#             self.tile_size_xy = database["tile_size_xy"]
#         else:
#             self.tile_size_xy = tile_size_xy
#         self.name=name
#         self.gui_tiles = GuiCheckBoxTile(self.tile_size_xy)
#         self.text = text
#         self.space = 10
#         #self.x = xy[0]
#         #self.y = xy[1]
#         font = pygame.font.SysFont("comicsansms", 12)
#         checkbox_text = font.render(self.text, True, 'BLUE')
#
#         self.img_unchecked = pygame.Surface((checkbox_text.get_width() + self.tile_size_xy[0] + self.space,
#                                              max(checkbox_text.get_height(), self.gui_tiles.height)),
#                                             pygame.SRCALPHA)
#         # pygame.draw.rect(surf,"white",surf.get_rect())
#
#         xy_for_checkbox = get_xy_for_centralized((self.img_unchecked.get_width(), self.img_unchecked.get_height()),
#                                                  (self.gui_tiles.width, self.gui_tiles.height))
#
#         self.img_checked = self.img_unchecked.copy()
#         self.img_unchecked.blit(self.gui_tiles.Unchecked, (0, xy_for_checkbox[1]))
#         self.img_checked.blit(self.gui_tiles.Checked, (0, xy_for_checkbox[1]))
#         xy_for_text = get_xy_for_centralized((self.img_unchecked.get_width(), self.img_unchecked.get_height()),
#                                              (checkbox_text.get_width(), checkbox_text.get_height()))
#         self.img_checked.blit(checkbox_text, (xy_for_text[0] + self.space, xy_for_text[1]))
#         self.img_unchecked.blit(checkbox_text, (xy_for_text[0] + self.space, xy_for_text[1]))
#         self.image = self.img_unchecked
#         self.rect = self.image.get_rect()
#         self.rect = self.rect.move(get_xy(px_parent_xy, self.tile_size_xy, start_in_tiles_xy[0], start_in_tiles_xy[1]))
#
#     def draw(self,surface):
#         surface.blit(self.image,self.rect)
#
#     def hoover(self,**kwargs):
#         pass
#     def LMB_down(self):
#         pass
#     def LMB_up(self):
#         pass
#     def RMB_down(self):
#         pass
#     def RMB_up(self):
#         pass
#
#     # def update(self, database, turret_database, text_upgrade=""):
#     #
#     #     if turret_database is not None and self.text == turret_database["TARGET_TYPE"]:
#     #         self.image = self.img_checked
#     #     else:
#     #         self.image = self.img_unchecked
#
#     # def LMB_down(self, parent_object, database=None):
#     #     parent_object.target_type = self.text
#     #     return {}
#     #
#     # def hover(self, selected_object, database):
#     #     return {}


class MenuButton(pygame.sprite.Sprite):
    def __init__(self,px_parent_xy:tuple,database:dict,start_in_tiles_xy,size_in_tiles_xy:tuple,name:str,text:str,parent_object=None,tile_size_xy:tuple=None,font_size=None,action=None,color=0,is_active=True):
        pygame.sprite.Sprite.__init__(self)
        self.text=text
        self.is_active=is_active
        self.is_pressed = False
        self.parent_object=parent_object
        self.is_hoovered = False
        self.name=name
        self.start_in_tiles_xy=start_in_tiles_xy
        self.frame_size_xy = (4, 4)
        if tile_size_xy is None:
            self.tile_size_xy = database["tile_size_xy"]
        else:
            self.tile_size_xy = tile_size_xy
        if font_size is None:
            self.font_size=get_font_size_no_bigger_then("comicsansms",floor(size_in_tiles_xy[1]*self.frame_size_xy[1]*0.8),database["font_sizes"])
        else:
            self.font_size = font_size
        self.frames_countdown=0
        self.action=action
        self.img2 = cropp_img2("img/GUI/2 Buttons/ButtonsMap.png", (4, 4), (color * 18, 54), 9, 2, 2, 3, "white")
        self.img = cropp_img2("img/GUI/2 Buttons/ButtonsMap.png", (4, 4), (color * 18, 36), 9, 2, 2, 3, "white")


        surf=pygame.surface.Surface((self.frame_size_xy[0]*size_in_tiles_xy[0],self.frame_size_xy[1]*size_in_tiles_xy[1]))

        surf.blit(self.img[0],(0,0))
        for i in range(1,size_in_tiles_xy[0]-1): surf.blit(self.img[1],(i*self.frame_size_xy[0],0))
        surf.blit(self.img[2], ((size_in_tiles_xy[0]-1)*self.frame_size_xy[0], 0))

        for j in range(1,size_in_tiles_xy[1]-1):
            surf.blit(self.img[3],(0,j*self.frame_size_xy[1]))
            for i in range(1,size_in_tiles_xy[0]-1): surf.blit(self.img[4],(i*self.frame_size_xy[0],j*self.frame_size_xy[1]))
            surf.blit(self.img[5], ((size_in_tiles_xy[0]-1)*self.frame_size_xy[0], j*self.frame_size_xy[1]))

        surf.blit(self.img[6],(0,self.frame_size_xy[1]*(size_in_tiles_xy[1]-1)))
        for i in range(1,size_in_tiles_xy[0]-1): surf.blit(self.img[7],(i*self.frame_size_xy[0],self.frame_size_xy[1]*(size_in_tiles_xy[1]-1)))
        surf.blit(self.img[8], ((size_in_tiles_xy[0]-1)*self.frame_size_xy[0], (size_in_tiles_xy[1]-1)*self.frame_size_xy[1]))

        surf2 = pygame.surface.Surface((self.frame_size_xy[0] * size_in_tiles_xy[0], self.frame_size_xy[1] * size_in_tiles_xy[1]))

        surf2.blit(self.img2[0], (0, 0))
        for i in range(1, size_in_tiles_xy[0] - 1): surf2.blit(self.img2[1], (i * self.frame_size_xy[0], 0))
        surf2.blit(self.img2[2], ((size_in_tiles_xy[0] - 1) * self.frame_size_xy[0], 0))

        for j in range(1, size_in_tiles_xy[1] - 1):
            surf2.blit(self.img2[3], (0, j * self.frame_size_xy[1]))
            for i in range(1, size_in_tiles_xy[0] - 1): surf2.blit(self.img2[4],
                                                      (i * self.frame_size_xy[0], j * self.frame_size_xy[1]))
            surf2.blit(self.img2[5], ((size_in_tiles_xy[0] - 1) * self.frame_size_xy[0], j * self.frame_size_xy[1]))

        surf2.blit(self.img2[6], (0, self.frame_size_xy[1] * (size_in_tiles_xy[1] - 1)))
        for i in range(1, size_in_tiles_xy[0] - 1): surf2.blit(self.img2[7],
                                                  (i * self.frame_size_xy[0], self.frame_size_xy[1] * (size_in_tiles_xy[1] - 1)))
        surf2.blit(self.img2[8], ((size_in_tiles_xy[0] - 1) * self.frame_size_xy[0], (size_in_tiles_xy[1] - 1) * self.frame_size_xy[1]))


        font = pygame.font.SysFont("comicsansms", self.font_size)
        button_text = font.render(self.text, True, 'White')
        tmp_xy=get_xy_for_centralized(surf.get_size(), button_text.get_size())
        surf.blit(button_text, tmp_xy)
        surf2.blit(button_text, tmp_xy)

        #pygame.draw.rect(surf,"white",pygame.rect.Rect(tmp_xy[0],tmp_xy[1],button_text.get_width(),button_text.get_height()),1)



        self.image_up=pygame.transform.smoothscale(surf2,(self.tile_size_xy[0]*size_in_tiles_xy[0]/4,self.tile_size_xy[1]*size_in_tiles_xy[1]/4))

        self.image=self.image_up
        self.rect=self.image.get_rect().move(get_xy(px_parent_xy, self.tile_size_xy, start_in_tiles_xy[0], start_in_tiles_xy[1]))

        #self.image_down=pygame.transform.scale(surf,(self.tile_size_xy[0]*size_in_tiles_xy[0]/4,self.tile_size_xy[1]*size_in_tiles_xy[1]/4))
        self.image_down=pygame.transform.smoothscale(surf,(self.tile_size_xy[0]*size_in_tiles_xy[0]/4,self.tile_size_xy[1]*size_in_tiles_xy[1]/4))
        #self.image_down = surf
        #pygame.draw.rect(self.image_up,"white",self.image_up.get_rect(),1)


    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def update(self,**kwargs):
        new_px_parent_xy=kwargs.get("px_parent_xy",None)
        if new_px_parent_xy is not None:
            self.px_parent_xy = new_px_parent_xy
            self.rect = self.image.get_rect().move(
                get_xy(self.px_parent_xy, self.tile_size_xy, self.start_in_tiles_xy[0], self.start_in_tiles_xy[1]))

        if self.is_pressed:
            self.image = self.image_down
        else:
            self.image = self.image_up

        if self.is_hoovered == False:
            self.is_pressed = False
        self.is_hoovered = False

    def hoover(self,**kwargs):
        self.is_hoovered=True
        if self.action=="upgrade_turret":
            self.parent_object.db["dmg_change"]=str(self.parent_object.db["dmg_upgrade"])
            self.parent_object.db["range_change"] = str(self.parent_object.db["range_upgrade"])
            self.parent_object.db["atsp_change"] = str(self.parent_object.db["atsp_upgrade"])
            sent_action_event("set_gold_change",gold_change=-self.parent_object.db["upgrade_price"])
        if self.action=="sell_turret":
            sent_action_event("set_gold_change", gold_change=-self.parent_object.db["sell_price"])
        if self.action == "upgrade_gold":
            sent_action_event("set_gems_change", gems_change=-1)
        if self.action == "upgrade_lives":
            sent_action_event("set_gems_change", gems_change=-1)
        if self.action == "armory_upgrade_turret":
            sent_action_event("set_armory_change", name=self.name)
            print(self.name)


    def LMB_down(self):
        self.is_pressed = True

    def LMB_up(self):
        if self.is_pressed and self.is_active:
            if self.action is not None:
                sent_action_event(action=self.action,button_name=self.name,parent_object=self.parent_object)
        self.is_pressed = False

    def RMB_down(self):
        pass
    def RMB_up(self):
        pass



class GuiGrid(pygame.sprite.Sprite):
    def __init__(self,px_parent_xy:tuple,database:dict,start_in_tiles_xy,size_in_tiles_xy:tuple,name:str,tile_size_xy:tuple=None):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.number_of_items_attached=0
        self.px_parent_xy=px_parent_xy
        self.start_in_tiles_xy=start_in_tiles_xy
        self.size_in_tiles_xy=size_in_tiles_xy
        self.members_group=pygame.sprite.Group()
        self.occupied_xy_blank = [[False] * self.size_in_tiles_xy[1] for i in range(self.size_in_tiles_xy[0])]
        self.occupied_xy=[[False]*self.size_in_tiles_xy[1] for i in range(self.size_in_tiles_xy[0])]
        if tile_size_xy is None:
            self.tile_size_xy = database["tile_size_xy"]
        else:
            self.tile_size_xy = tile_size_xy

        self.px_start_xy = get_xy(px_parent_xy, self.tile_size_xy, start_in_tiles_xy[0], start_in_tiles_xy[1])
        self.px_size_xy = (size_in_tiles_xy[0] * self.tile_size_xy[0], size_in_tiles_xy[1] * self.tile_size_xy[1])
        self.image = pygame.Surface((self.px_size_xy[0], self.px_size_xy[1]))
        self.image.set_colorkey((0, 0, 0))

        self.rect = pygame.rect.Rect(self.px_start_xy[0], self.px_start_xy[1], self.px_size_xy[0], self.px_size_xy[1])

    def add(self, sprite: pygame.sprite.Sprite):
        self.members_group.add(sprite)
        if type(sprite)==ItemMenu: self.number_of_items_attached+=1
        return get_member_by_name(self.members_group.sprites(), sprite.name)
    def remove(self, sprite: pygame.sprite.Sprite):
        if type(sprite) == ItemMenu:
            self.number_of_items_attached -= 1
            sprite.remove(self.members_group)
            #self.members_group.sprites().remove(sprite)

    def draw(self,surface):
        surface.blit(self.image,self.rect)
        for mm in self.members_group.sprites(): mm.draw(surface)

    def update(self,**kwargs):
        new_px_parent_xy=kwargs.get("px_parent_xy",None)
        if new_px_parent_xy is not None:
            self.px_parent_xy = new_px_parent_xy
            self.px_start_xy = get_xy(self.px_parent_xy, self.tile_size_xy, self.start_in_tiles_xy[0], self.start_in_tiles_xy[1])
            self.px_size_xy = (self.size_in_tiles_xy[0] * self.tile_size_xy[0], self.size_in_tiles_xy[1] * self.tile_size_xy[1])

            self.image = pygame.Surface((self.px_size_xy[0], self.px_size_xy[1]))
            self.image.set_colorkey((0, 0, 0))


        for i in range(self.size_in_tiles_xy[0]):
            for j in range(self.size_in_tiles_xy[1]):
                pygame.draw.rect(self.image, (255, 255, 255),
                                 pygame.rect.Rect(self.tile_size_xy[0] * i, self.tile_size_xy[1] * j,
                                                  self.tile_size_xy[0], self.tile_size_xy[1]), 1)

                #if self.occupied_xy[i][j]:
                    #s = pygame.Surface((self.tile_size_xy[0]-2,self.tile_size_xy[1]-2))
#                        s.set_alpha(5)
                    #s.fill((186,100,100))
                    #self.image.blit(s, (self.tile_size_xy[0] * i+1, self.tile_size_xy[1] * j+1))

                if  self.occupied_xy[i][j]: pygame.draw.rect(self.image, (186,100,100),pygame.rect.Rect(self.tile_size_xy[0] * i+1,self.tile_size_xy[1] * j+1,self.tile_size_xy[0]-2,self.tile_size_xy[1]-2))


            self.rect = pygame.rect.Rect(self.px_start_xy[0], self.px_start_xy[1], self.px_size_xy[0],
                                         self.px_size_xy[1])

        self.occupied_xy=[[False] * self.size_in_tiles_xy[1] for i in range(self.size_in_tiles_xy[0])]


        self.members_group.update(px_parent_xy=self.px_start_xy,allowed_map=kwargs.get("allowed_map",None))

    def hoover(self,**kwargs):
        MM_list=kwargs.get("MM_list",None)
        if MM_list is not None:
            for MM in MM_list:
                for mm in MM:
                    #print(type(MM[mm]))
                    if type(MM[mm])==ItemMenu:
                        if MM[mm].anchor_to_mouse:
                            MM[mm].parent_grid=self

    def LMB_down(self):
        pass
    def LMB_up(self):
        pass
    def RMB_down(self):
        pass
    def RMB_up(self):
        pass


def create_inventory_menu(database):
    IM={}
    inv_menu = pygame.sprite.Group()

    inv_menu.add(MenuTitle((0,0), database, (0, 0),(15,15), "TitleMenue","TITLE_1_witam Marek",tile_size_xy=database["double_tile_size_xy"]))
    IM['TitleMenue'] =get_member_by_name(inv_menu.sprites(), "TitleMenue")



    IM['TitleMenue/grid1'] = IM['TitleMenue'].add(GuiGrid(IM['TitleMenue'].px_start_xy, database, (0.5, 1.25),(14,13), "TitleMenue/grid1",tile_size_xy=database["double_tile_size_xy"]))

    IM['TitleMenue/button1'] = IM['TitleMenue'].add(
        MenuButton(IM['TitleMenue'].px_start_xy, database, (1, 4), (16, 8), "TitleMenue/button1", text="Add", color=3,action="create_test_menu"))

    return inv_menu,IM

def create_test_menu(database,index):
    IM={}
    inv_menu = pygame.sprite.Group()

    inv_menu.add(MenuTitle( get_xy((0,0),database["tile_size_xy"],55,37), database, (0, 0),(8,5), "TestMenu"+str(index),"test TEST",tile_size_xy=database["double_tile_size_xy"]))
    IM['TestMenu'+str(index)] =get_member_by_name(inv_menu.sprites(), "TestMenu"+str(index))

    #IM['TestMenu'+str(index)+'/grid1'] = IM['TestMenu'+str(index)].add(GuiGrid(IM['TestMenu'+str(index)].px_start_xy, database, (0, 0),(16,10), "TestMenu"+str(index)+"/grid1",tile_size_xy=database["tile_size_xy"]))

    IM['TestMenu'+str(index)+'/button1'] = IM['TestMenu'+str(index)].add(MenuButton(IM['TestMenu'+str(index)].px_start_xy, database, (1, 4),(52,8), "TestMenu/button1",text="Guzior",color=3))
    IM['TestMenu'+str(index)+'/button2'] = IM['TestMenu'+str(index)].add(
        MenuButton(IM['TestMenu'+str(index)].px_start_xy, database, (15, 0), (4, 4), "TestMenu"+str(index)+"/button2", text="X", color=3,action="close_root_menu"))

    #IM['TestMenu/button2'] = IM['TestMenu'].add(MenuButton(IM['TestMenu'].px_start_xy, database, (0, 0),(64,8), "TestMenu/button2",text="Guzior",color=3))

    IM['TestMenu'+str(index)+'/text1'] = IM['TestMenu'+str(index)].add(
        MenuText(IM['TestMenu'+str(index)].px_start_xy, database, (1, 7), "TestMenu"+str(index)+"/text1","init txt"))

    return inv_menu,IM

def create_chest_menu(database):
    IM={}
    inv_menu = pygame.sprite.Group()

    inv_menu.add(MenuTitle( get_xy((0,0),database["tile_size_xy"],55,15), database, (0, 0),(8,5), "ChestMenu","chest",tile_size_xy=database["double_tile_size_xy"]))
    IM['ChestMenu'] =get_member_by_name(inv_menu.sprites(), "ChestMenu")

    IM['ChestMenu/grid1'] = IM['ChestMenu'].add(GuiGrid(IM['ChestMenu'].px_start_xy, database, (0.5, 1.25),(7,3), "ChestMenu/grid1",tile_size_xy=database["double_tile_size_xy"]))


    IM['ChestMenu/grid1/item_1'] = IM['ChestMenu/grid1'].add(
        ItemMenu(IM['ChestMenu/grid1'].px_start_xy, database, (2, 0),  "ChestMenu/grid1/item_1",tile_size_xy=database["double_tile_size_xy"],item_name="shirt",parent_grid=IM['ChestMenu/grid1']))




    return inv_menu,IM

def find_colliding_objects(mouse_pos:tuple,MM_list:list,turrets):
    ret=[]
    for MM in MM_list:
        for obj in MM:
            if MM[obj].rect.collidepoint(mouse_pos): ret.append(MM[obj])
    for MM in turrets:
        if MM.rect.collidepoint(mouse_pos): ret.append(MM)
    return ret



def close_root_menu_action(AllMenus:list):
    pass

def get_xy_index_from_px(point:tuple,start_in_tiles_xy:tuple,px_start_xy:tuple,tile_size_xy:tuple):
    offset=(start_in_tiles_xy[0]*tile_size_xy[0],start_in_tiles_xy[1]*tile_size_xy[1])

    #if point[0]>=px_start_xy[0] and point[1]>=px_start_xy[1]:
    x=floor((point[0]-px_start_xy[0]-offset[0]+(tile_size_xy[0]/2))/tile_size_xy[0])
    y=floor((point[1]-px_start_xy[1]-offset[1]+(tile_size_xy[1]/2))/tile_size_xy[1])
    ### (tile_size_xy[0]/2) part is for fixing to center of square rather than top left corner

    return x,y

def detect_menu_mouse_hoover(MM_list:list):
    for MM in MM_list:
        mousepoint = pygame.mouse.get_pos()
        for obj in MM:
            if MM[obj].rect.collidepoint(mousepoint):
                MM[obj].hoover(MM_list=MM_list)

def handle_LMB_down(colliding_objects,mouse_pos):
    #for obj in colliding_objects:
    #    obj.click()
    if len(colliding_objects)>0: colliding_objects[-1].LMB_down()


def handle_RMB_down(colliding_objects,mouse_pos):
    for obj in colliding_objects:
        obj.RMB_down()

def handle_LMB_up(colliding_objects,mouse_pos):
    for obj in colliding_objects:
        obj.LMB_up()

def handle_RMB_up(colliding_objects,mouse_pos):
    pass

def bring_root_to_front(clicked_object,All_menus):
    tmp=None

    if len(clicked_object)>0 and type(clicked_object[-1])!=TurretSprite:
    #if len(clicked_object) > 0 :
        for i in range(len(All_menus)):
            #print(clicked.name)
            if clicked_object[-1].name in All_menus[i][1].keys():
                tmp=i


    if tmp is not None:

        All_menus.append(All_menus.pop(tmp))
    return All_menus

def sent_action_event(action:str,**kwargs):
    if action=="close_root_menu":
        button_name=kwargs.get("button_name",None)
        ev_dic = {
            "action": "close_root_menu",
            "button_name": button_name
        }
    if action=="quit_game":
        ev_dic = {
            "action": "quit_game"
        }
    if action=="mainmenu":
        ev_dic = {
            "action": "mainmenu"
        }
    if action=="start_new_game":
        ev_dic = {
            "action": "start_new_game"
        }
    if action=="upgrade_gold":
        ev_dic = {
            "action": "upgrade_gold"
        }
    if action=="upgrade_lives":
        ev_dic = {
            "action": "upgrade_lives"
        }
    if action=="armory_upgrade_turret":
        ev_dic = {
            "action": "armory_upgrade_turret",
            "button_name": kwargs.get("button_name", None)
        }


    if action == "create_test_menu":
        ev_dic = {
            "action": "create_test_menu"
        }
    if action == "move_item_from_grid_to_grid":

        ev_dic = {
            "action": "move_item_from_grid_to_grid",
            "item": kwargs.get("item", None),
            "old_grid": kwargs.get("old_grid", None),
            "new_grid": kwargs.get("new_grid", None),
            "new_grid_start_in_tiles_xy": kwargs.get("new_grid_start_in_tiles_xy", None),
            "tile_size_xy": kwargs.get("tile_size_xy", None)
        }
    if action == "start_battle":
        ev_dic = {
            "action": "start_battle",
            "button_name": kwargs.get("button_name",None)
        }

    if action == "next_wave":
        ev_dic = {
            "action": "next_wave",
            "button_name": kwargs.get("button_name", None)
        }

    if action == "build_turret":
        ev_dic = {
            "action": "build_turret",
            "turret": kwargs.get("turret", None),
        }
    if action == "sell_turret":
        ev_dic = {
            "action": "sell_turret",
            "button_name": kwargs.get("button_name", None),
            "parent_object": kwargs.get("parent_object", None),
        }
    if action == "upgrade_turret":
        ev_dic = {
            "action": "upgrade_turret",
            "button_name": kwargs.get("button_name", None),
            "parent_object": kwargs.get("parent_object", None),
        }
    if action == "set_gold_change":
        ev_dic={
            "action": "set_gold_change",
            "gold_change": kwargs.get("gold_change", None)
        }
    if action == "set_gems_change":
        ev_dic={
            "action": "set_gems_change",
            "gems_change": kwargs.get("gems_change", None)
        }
    if action == "set_armory_change":
        ev_dic={
            "action": "set_armory_change",
            "name": kwargs.get("name", None)
        }
    if action == "open_shop":
        ev_dic = {
            "action": "open_shop"
        }
    if action == "open_armory":
        ev_dic = {
            "action": "open_armory"
        }

    ev = pygame.event.Event(pygame.USEREVENT, ev_dic)
    pygame.event.post(ev)

def move_item_from_grid_to_grid(ev_dic:dict,All_menus_groups_ordered,database):

    ### Add Item
    new_item_name = ev_dic["new_grid"].name + "/item_" + str(ev_dic["new_grid"].number_of_items_attached)
    new_item_index = None
    for j in range(len(All_menus_groups_ordered)):
        if ev_dic["new_grid"].name in All_menus_groups_ordered[j][1].keys():
            new_item_index = j

    All_menus_groups_ordered[new_item_index][1][new_item_name] = ev_dic["new_grid"].add(
        ItemMenu(ev_dic["new_grid"].px_start_xy, database, ev_dic["new_grid_start_in_tiles_xy"], new_item_name,
                 tile_size_xy=ev_dic["tile_size_xy"], item_name=ev_dic["item"].item.name, parent_grid=ev_dic["new_grid"]))

    ### REMOVE ITEM

    ev_dic["old_grid"].remove(ev_dic["item"])

    for i in range(len(All_menus_groups_ordered)):
        if ev_dic["old_grid"].name in All_menus_groups_ordered[i][1].keys():
            old_item=All_menus_groups_ordered[i][1]
            old_item.pop(ev_dic["item"].name)



def generate_world_prices_and_enemies():
    ret={}
    ret["enemies"]={}
    ret["prices"]={}
    #Enemies
    for i in range(5):
        ret["enemies"][i]=[]
        for j in range(len(available_enemies)):
            if randint(0,1)==1:
                ret["enemies"][i].append(available_enemies[j])
            if len(ret["enemies"][i]) == 0: ret["enemies"][i].append(available_enemies[randint(0, len(available_enemies)-1)])

    i=5
    ret["enemies"][i]= ["eye","goblin","skeleton","spider"]



    #ret_wave=wave_generator(ret["enemies"])

    for i in range(5):
        ret["prices"][i]=[]
        for j in range(len(available_prices)):
            if randint(0,1)==1 and len(ret["prices"][i])<3:
                ret["prices"][i].append(available_prices[j])
        if len(ret["prices"][i])==0: ret["prices"][i].append(available_prices[randint(0,len(available_prices)-1)])

    i=5
    ret["prices"][i]=["victory"]


    return ret












from math import ceil
def create_main_menu(database):
    MM={}
    main_menu = pygame.sprite.Group()



    main_menu.add(MenuTitle( get_xy((0,0),database["tile_size_xy"],0,0), database, (database["resolution_in_tiles_percent_xy"][25][0],database["resolution_in_tiles_percent_xy"][40][1]),(database["resolution_in_tiles_percent_xy"][50][0],database["resolution_in_tiles_percent_xy"][20][1]), "MainMenu","",tile_size_xy=database["tile_size_xy"],draggable=False))
    MM['MainMenu'] =get_member_by_name(main_menu.sprites(), "MainMenu")


    MM['MainMenu/button1'] = MM['MainMenu'].add(
        MenuButton(MM['MainMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][15][0], 2), (database["resolution_in_tiles_percent_xy"][20][0]*4, 8), "MainMenu/button1", text="Start new game", color=3,action="start_new_game"))

    MM['MainMenu/button2'] = MM['MainMenu'].add(
        MenuButton(MM['MainMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][15][0], 5), (database["resolution_in_tiles_percent_xy"][20][0]*4, 8), "MainMenu/button2", text="Restart", color=3,action="restart_game"))

    MM['MainMenu/button3'] = MM['MainMenu'].add(
        MenuButton(MM['MainMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][15][0], 8), (database["resolution_in_tiles_percent_xy"][20][0]*4, 8), "MainMenu/button3", text="Quit", color=3,action="quit_game"))

    return main_menu,MM



def create_world_menu(database):
    database["world_prices_and_enemies"]=generate_world_prices_and_enemies()
    LM = {}
    level_menu = pygame.sprite.Group()

    level_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                            (database["resolution_in_tiles_percent_xy"][0][0],
                             database["resolution_in_tiles_percent_xy"][0][1]),
                            (database["resolution_in_tiles_percent_xy"][110][0],
                             database["resolution_in_tiles_percent_xy"][110][1]), "LevelMenu", "",
                            tile_size_xy=database["tile_size_xy"], draggable=False))
    LM['LevelMenu'] = get_member_by_name(level_menu.sprites(), "LevelMenu")

    lvl_menu_grid=([5],[20])
    coords_x=0
    coords_y=0

    ### CENTER
    #LM['LevelMenu/Title0'] = LM['LevelMenu'].add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,(database["resolution_in_tiles_percent_xy"][lvl_menu_grid[0][coords_x]][0],database["resolution_in_tiles_percent_xy"][lvl_menu_grid[1][coords_y]][1]),(database["resolution_in_tiles_percent_xy"][30][0],database["resolution_in_tiles_percent_xy"][15][1]), "LevelMenu/Title0", "Title0",tile_size_xy=database["double_tile_size_xy"], draggable=True))
    LM['LevelMenu/Title0'] = LM['LevelMenu'].add(MenuTitle(LM['LevelMenu'].px_start_xy, database, (
        database["resolution_in_tiles_percent_xy"][lvl_menu_grid[0][coords_x]][0],
        database["resolution_in_tiles_percent_xy"][lvl_menu_grid[1][coords_y]][1]),
                                                           (database["resolution_in_tiles_percent_xy"][40][0],
                                                            database["resolution_in_tiles_percent_xy"][15][1]),
                                                           "LevelMenu/Title0", "Title0",
                                                           tile_size_xy=database["double_tile_size_xy"],
                                                           draggable=True))




    LM['LevelMenu/Title0/button0'] = LM['LevelMenu/Title0'].add(
        MenuButton(LM['LevelMenu/Title0'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][67][0], 3),
                   (database["resolution_in_tiles_percent_xy"][10][0] * 4, 8), "LevelMenu/Title0/button0",
                   text="Shop", color=3, action="open_shop"))

    LM['LevelMenu/Title0/button1'] = LM['LevelMenu/Title0'].add(
        MenuButton(LM['LevelMenu/Title0'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][67][0], 6),
                   (database["resolution_in_tiles_percent_xy"][10][0] * 4, 8), "LevelMenu/Title0/button1",
                   text="Armory", color=3, action="open_armory"))


    ### ACTIVE
    LM['LevelMenu/Title0/Title0'] = LM['LevelMenu/Title0'].add(
        MenuTitle(LM['LevelMenu/Title0'].px_start_xy, database,
                  (1,1),
                  (5,6), "LevelMenu/Title0/Title0", "Active",
                  tile_size_xy=database["double_tile_size_xy"], draggable=False))

    LM['LevelMenu/Title0/Title0/gridActive'] = LM['LevelMenu/Title0/Title0'].add(GuiGrid(LM['LevelMenu/Title0/Title0'].px_start_xy, database, (0.25, 0.70),(2,2), "LevelMenu/Title0/Title0/gridActive",tile_size_xy=database["quadrupal_tile_size_xy"]))

    ### INACTIVE
    LM['LevelMenu/Title0/Title1'] = LM['LevelMenu/Title0'].add(
        MenuTitle(LM['LevelMenu/Title0'].px_start_xy, database,
                  (8, 1),
                  (9, 6), "LevelMenu/Title0/Title1", "InActive",
                  tile_size_xy=database["double_tile_size_xy"], draggable=False))
    LM['LevelMenu/Title0/Title1/gridInActive'] = LM['LevelMenu/Title0/Title1'].add(GuiGrid(LM['LevelMenu/Title0/Title0'].px_start_xy, database, (0.25, 0.7),(4,2), "LevelMenu/Title0/Title1/gridInActive",tile_size_xy=database["quadrupal_tile_size_xy"]))

    inactive_item_index=0

    for item in database["available_turrets"]:
        LM['LevelMenu/Title0/Title1/gridInActive/item'+str(inactive_item_index)] = LM['LevelMenu/Title0/Title1/gridInActive'].add(
        ItemMenu(LM['LevelMenu/Title0/Title1/gridInActive'].px_start_xy, database, (inactive_item_index, 0),  "LevelMenu/Title0/Title1/gridInActive/item"+str(inactive_item_index),tile_size_xy=database["quadrupal_tile_size_xy"],item_name=item,parent_grid=LM['LevelMenu/Title0/Title1/gridInActive']))
        inactive_item_index+=1

    ###  Resorces
    LM['LevelMenu/Title0/Title2'] = LM['LevelMenu/Title0'].add(
        MenuTitle(LM['LevelMenu/Title0'].px_start_xy, database,
                  (18, 1),
                  (5, 6), "LevelMenu/Title0/Title2", "Resources",
                  tile_size_xy=database["double_tile_size_xy"], draggable=False))

    LM['LevelMenu/Title0/Title2/TextFood'] = LM['LevelMenu/Title0/Title2'].add(
        MenuText(LM['LevelMenu/Title0/Title2'].px_start_xy, database, (1, 3), "LevelMenu/Title0/Title2/TextFood","Food: "))
    LM['LevelMenu/Title0/Title2/TextFood_change'] = LM['LevelMenu/Title0/Title2'].add(
        MenuText(LM['LevelMenu/Title0/Title2'].px_start_xy, database, (7, 3), "LevelMenu/Title0/Title2/TextFood_change", "",variable_name="food_change"))

    LM['LevelMenu/Title0/Title2/TextGems'] = LM['LevelMenu/Title0/Title2'].add(
        MenuText(LM['LevelMenu/Title0/Title2'].px_start_xy, database, (1, 5), "LevelMenu/Title0/Title2/TextGems","Gems: "))

    LM['LevelMenu/Title0/Title2/TextGems_change'] = LM['LevelMenu/Title0/Title2'].add(
        MenuText(LM['LevelMenu/Title0/Title2'].px_start_xy, database, (7, 5), "LevelMenu/Title0/Title2/TextGems_change", "",variable_name="gems_change"))

    LM['LevelMenu/Title0/Title3'] = LM['LevelMenu/Title0'].add(
        MenuTitle(LM['LevelMenu/Title0'].px_start_xy, database,
                  (24, 1),
                  (9, 6), "LevelMenu/Title0/Title3", "Details",
                  tile_size_xy=database["double_tile_size_xy"], draggable=False))

    ### WORLDS
    #lvl_menu_grid=([10,40,70],[10,75])
    lvl_menu_grid=([5,20,35],[5,37])  # Halved becouse double sized

    lvl_menu_size_xy=(12,15)

    bg={1:"img/graveyard.png",
        2: "img/volcano.png",
        3: "img/forest_fire.png",
        4: "img/island.png",
        5: "img/desert.png",
        6: "img/road.png"
        }
    index=1
    for coords_x in range(3):
        for coords_y in range(2):
            LM['LevelMenu/Title'+str(index)] = LM['LevelMenu'].add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                            (database["resolution_in_tiles_percent_xy"][lvl_menu_grid[0][coords_x]][0],
                             database["resolution_in_tiles_percent_xy"][lvl_menu_grid[1][coords_y]][1]),
                            (database["resolution_in_tiles_percent_xy"][lvl_menu_size_xy[0]][0],
                             database["resolution_in_tiles_percent_xy"][lvl_menu_size_xy[1]][1]), "Title"+str(index), "Level "+str(index),
                            tile_size_xy=database["double_tile_size_xy"], draggable=False,background=bg[index]))

            LM['LevelMenu/Title'+str(index)+'/buttonStartLvl'+str(index)] = LM['LevelMenu/Title'+str(index)].add(
                MenuButton(LM['LevelMenu/Title'+str(index)].px_start_xy, database,
                           (database["resolution_in_tiles_percent_xy"][10][0], database["resolution_in_tiles_percent_xy"][(lvl_menu_size_xy[1]*2)-6][1]),
                           (database["resolution_in_tiles_percent_xy"][6][0] * 4, 8), 'LevelMenu/Title'+str(index)+'/buttonStartLvl'+str(index),
                           text="To battle!", color=3, action="start_battle"))

            ### MOBS GRID
            LM['LevelMenu/Title'+str(index)+'/GridMobs'] = LM['LevelMenu/Title'+str(index)].add(
                GuiGrid(LM['LevelMenu/Title'+str(index)].px_start_xy, database, (0.5, 6.75), (4, 1),
                        'LevelMenu/Title'+str(index)+'/GridMobs', tile_size_xy=database["double_tile_size_xy"]))

            for i in range(len(database["world_prices_and_enemies"]["enemies"][index-1])):
                LM['LevelMenu/Title'+str(index)+'/GridMobs/ItemEnemy'+str(i)] = LM['LevelMenu/Title'+str(index)+'/GridMobs'].add(
                    ItemMenu(LM['LevelMenu/Title'+str(index)+'/GridMobs'].px_start_xy, database, (i, 0),
                             'LevelMenu/Title'+str(index)+'/GridMobs/ItemEnemy'+str(i),
                             tile_size_xy=database["double_tile_size_xy"], item_name=database["world_prices_and_enemies"]["enemies"][index-1][i],
                             parent_grid=LM['LevelMenu/Title'+str(index)+'/GridMobs'],draggable=False))




            ### PRICES GRID
            LM['LevelMenu/Title' + str(index) + '/GridPrices'] = LM['LevelMenu/Title' + str(index)].add(
                GuiGrid(LM['LevelMenu/Title' + str(index)].px_start_xy, database, (8.5, 6.75), (3, 1),
                        'LevelMenu/Title' + str(index) + '/GridPrices', tile_size_xy=database["double_tile_size_xy"]))

            for i in range(len(database["world_prices_and_enemies"]["prices"][index-1])):
                LM['LevelMenu/Title'+str(index)+'/GridPrices/ItemEnemy'+str(i)] = LM['LevelMenu/Title'+str(index)+'/GridPrices'].add(
                    ItemMenu(LM['LevelMenu/Title'+str(index)+'/GridPrices'].px_start_xy, database, (i, 0),
                             'LevelMenu/Title'+str(index)+'/GridPrices/ItemEnemy'+str(i),
                             tile_size_xy=database["double_tile_size_xy"], item_name=database["world_prices_and_enemies"]["prices"][index-1][i],
                             parent_grid=LM['LevelMenu/Title'+str(index)+'/GridPrices'],draggable=False))

            index+=1


    return level_menu,LM


def create_wave_menu(database):
    LM = {}
    level_menu = pygame.sprite.Group()
    menu_start_x_pt=100-database["wave_menu_width_pt"]
    menu_width_px=database["wave_menu_width_pt"]

    level_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                             (database["resolution_in_tiles_percent_xy"][menu_start_x_pt][0],
                              database["resolution_in_tiles_percent_xy"][0][1]),
                             (database["resolution_in_tiles_percent_xy"][menu_width_px][0],
                              database["resolution_in_tiles_percent_xy"][100][1]), "WaveMenu", "",
                             tile_size_xy=database["tile_size_xy"], draggable=False))
    LM['WaveMenu'] = get_member_by_name(level_menu.sprites(), "WaveMenu")

    ### STATS
    LM['WaveMenu/Stats']=LM['WaveMenu'].add(MenuTitle(LM['WaveMenu'].px_start_xy, database,
                             (0,0),
                             (database["resolution_in_tiles_percent_xy"][menu_width_px/2][0],
                              database["resolution_in_tiles_percent_xy"][10][1]), "WaveMenu/Stats", "Stats",
                             tile_size_xy=database["double_tile_size_xy"], draggable=False))

    LM['WaveMenu/Stats/Lives'] = LM['WaveMenu/Stats'].add(
        MenuText(LM['WaveMenu/Stats'].px_start_xy, database, (1, 3), "WaveMenu/Stats/Lives", "Lives: "))
    LM['WaveMenu/Stats/Gold'] = LM['WaveMenu/Stats'].add(
        MenuText(LM['WaveMenu/Stats'].px_start_xy, database, (1, 5), "WaveMenu/Stats/Gold", "Gold: "))
    LM['WaveMenu/Stats/GoldChange'] = LM['WaveMenu/Stats'].add(
        MenuText(LM['WaveMenu/Stats'].px_start_xy, database, (8, 5), "WaveMenu/Stats/GoldChange", database["gold_change"]))

    LM['WaveMenu/Stats/Wave'] = LM['WaveMenu/Stats'].add(
        MenuText(LM['WaveMenu/Stats'].px_start_xy, database, (1, 7), "WaveMenu/Stats/Wave", "Wave: "))

    LM['WaveMenu/Stats/NextWave']= LM['WaveMenu/Stats'].add(MenuButton(LM['WaveMenu/Stats'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][10][0], 2),
                   (database["resolution_in_tiles_percent_xy"][7][0] * 4, 8), "WaveMenu/Stats/NextWave",
                   text="Next Wave", color=3, action="next_wave"))

    ### DETAILS
    LM['WaveMenu/Details']=LM['WaveMenu'].add(MenuTitle(LM['WaveMenu'].px_start_xy, database,
                             (0,
                              database["resolution_in_tiles_percent_xy"][10][1]),
                             (database["resolution_in_tiles_percent_xy"][menu_width_px/2][0],
                              database["resolution_in_tiles_percent_xy"][20][1]), "WaveMenu/Details", "Details",
                             tile_size_xy=database["double_tile_size_xy"], draggable=False))
    ### SHOP
    LM['WaveMenu/Shop']=LM['WaveMenu'].add(MenuTitle(LM['WaveMenu'].px_start_xy, database,
                             (0,
                              database["resolution_in_tiles_percent_xy"][30][1]),
                             (database["resolution_in_tiles_percent_xy"][menu_width_px/2][0],
                              database["resolution_in_tiles_percent_xy"][17][1]), "WaveMenu/Shop", "Shop",
                             tile_size_xy=database["double_tile_size_xy"], draggable=False))
    LM['WaveMenu/Shop/grid0'] = LM['WaveMenu/Shop'].add(
        GuiGrid(LM['WaveMenu/Shop'].px_start_xy, database, (0.5, 1.25), (4, 1),
                "WaveMenu/Shop/grid0", tile_size_xy=database["quadrupal_tile_size_xy"]))

    shop_item_index=0
    for item in database["wave_shop_items"]:
        LM['WaveMenu/Shop/grid0/item' + str(shop_item_index)] = LM['WaveMenu/Shop/grid0'].add(
            ItemMenu(LM['WaveMenu/Shop/grid0'].px_start_xy, database, (shop_item_index, 0),
                     "WaveMenu/Shop/grid0/item" + str(shop_item_index),
                     tile_size_xy=database["quadrupal_tile_size_xy"], item_name=item,
                     parent_grid=LM['WaveMenu/Shop/grid0']))
        shop_item_index+=1
    #
    # LM['WaveMenu/Shop/grid0/item' + str(shop_item_index)] = LM['WaveMenu/Shop/grid0'].add(
    #     ItemMenu(LM['WaveMenu/Shop/grid0'].px_start_xy, database, (0, 0),
    #              "WaveMenu/Shop/grid0/item" + str(shop_item_index),
    #              tile_size_xy=database["quadrupal_tile_size_xy"], item_name="catapult",
    #              parent_grid=LM['WaveMenu/Shop/grid0']))
    # shop_item_index = 1
    # LM['WaveMenu/Shop/grid0/item' + str(shop_item_index)] = LM['WaveMenu/Shop/grid0'].add(
    #     ItemMenu(LM['WaveMenu/Shop/grid0'].px_start_xy, database, (1, 0),
    #              "WaveMenu/Shop/grid0/item" + str(shop_item_index),
    #              tile_size_xy=database["quadrupal_tile_size_xy"], item_name="archer",
    #              parent_grid=LM['WaveMenu/Shop/grid0']))

    ###INFO
    LM['WaveMenu/Info']=LM['WaveMenu'].add(MenuTitle(LM['WaveMenu'].px_start_xy, database,
                             (0,
                              database["resolution_in_tiles_percent_xy"][45][1]),
                             (database["resolution_in_tiles_percent_xy"][menu_width_px/2][0],
                              database["resolution_in_tiles_percent_xy"][10][1]), "WaveMenu/Info", "Info",
                             tile_size_xy=database["double_tile_size_xy"], draggable=False))
    LM['WaveMenu/Info/Debug0'] = LM['WaveMenu/Info'].add(
        MenuText(LM['WaveMenu/Info'].px_start_xy, database, (1, 2), "WaveMenu/Info/Debug0", "debug0: "))
    LM['WaveMenu/Info/Debug1'] = LM['WaveMenu/Info'].add(
        MenuText(LM['WaveMenu/Info'].px_start_xy, database, (1, 3), "WaveMenu/Info/Debug1", "Debug1: "))

    return level_menu, LM

def create_wave_turret_details(wave_menu,selected_turret,database,destroy=False):

    if not destroy:
        i=0
        for target_type in [
            ("furthest",(1,3)),
            ("closest",(10,3)),
            ("most_hp",(1,5)),
            ("least_hp",(10,5))
        ]:
            wave_menu['WaveMenu/Details/Checkbox'+str(i)] = wave_menu['WaveMenu/Details'].add(
        GuiCheckbox(wave_menu['WaveMenu/Details'].px_start_xy, target_type[1], database["tile_size_xy"],
                    "WaveMenu/Details/Checkbox"+str(i), target_type[0], database["tile_size_xy"], selected_turret, True))
            i+=1

        wave_menu['WaveMenu/Details/ButtonSell'] = wave_menu['WaveMenu/Details'].add(MenuButton(wave_menu['WaveMenu/Details'].px_start_xy, database, (1,7),(database["resolution_in_tiles_percent_xy"][10][0] * 4, 8), "WaveMenu/Details/ButtonSell",text="Sell",parent_object=selected_turret, color=3, action="sell_turret"))
        wave_menu['WaveMenu/Details/ButtonUpgrade'] = wave_menu['WaveMenu/Details'].add(MenuButton(wave_menu['WaveMenu/Details'].px_start_xy, database, (1,9),(database["resolution_in_tiles_percent_xy"][10][0] * 4, 8), "WaveMenu/Details/ButtonUpgrade",text="Upgrade",parent_object=selected_turret, color=3, action="upgrade_turret"))


        wave_menu['WaveMenu/Details/TxtDMG'] = wave_menu['WaveMenu/Details'].add(
            MenuText(wave_menu['WaveMenu/Details'].px_start_xy, database, (1, 11), "LevelMenu/Details/TxtDMG", "DMG"))
        wave_menu['WaveMenu/Details/TxtDMGValue'] = wave_menu['WaveMenu/Details'].add(
            MenuText(wave_menu['WaveMenu/Details'].px_start_xy, database, (6, 11), "LevelMenu/Details/TxtDMGValue", "DMG",parent_object=selected_turret,variable_name="dmg"))
        wave_menu['WaveMenu/Details/TxtDMGValueChange'] = wave_menu['WaveMenu/Details'].add(
            MenuText(wave_menu['WaveMenu/Details'].px_start_xy, database, (11, 11), "LevelMenu/Details/TxtDMGValueChange", "DMG",parent_object=selected_turret,variable_name="dmg_change"))

        wave_menu['WaveMenu/Details/TxtRange'] = wave_menu['WaveMenu/Details'].add(
            MenuText(wave_menu['WaveMenu/Details'].px_start_xy, database, (1, 13), "LevelMenu/Details/TxtRange", "Range"))
        wave_menu['WaveMenu/Details/TxtRangeValue'] = wave_menu['WaveMenu/Details'].add(
            MenuText(wave_menu['WaveMenu/Details'].px_start_xy, database, (6, 13), "LevelMenu/Details/TxtRangeValue", "Range",parent_object=selected_turret,variable_name="range"))
        wave_menu['WaveMenu/Details/TxtRangeValueChange'] = wave_menu['WaveMenu/Details'].add(
            MenuText(wave_menu['WaveMenu/Details'].px_start_xy, database, (11, 13), "LevelMenu/Details/TxtRangeValueChange", "Range",parent_object=selected_turret,variable_name="range_change"))

        wave_menu['WaveMenu/Details/TxtATSP'] = wave_menu['WaveMenu/Details'].add(
            MenuText(wave_menu['WaveMenu/Details'].px_start_xy, database, (1, 15), "LevelMenu/Details/TxtATSP", "ATSP"))
        wave_menu['WaveMenu/Details/TxtATSPValue'] = wave_menu['WaveMenu/Details'].add(
            MenuText(wave_menu['WaveMenu/Details'].px_start_xy, database, (6, 15), "LevelMenu/Details/TxtATSPValue", "ATSP",parent_object=selected_turret,variable_name="atsp"))
        wave_menu['WaveMenu/Details/TxtATSPValueChange'] = wave_menu['WaveMenu/Details'].add(
            MenuText(wave_menu['WaveMenu/Details'].px_start_xy, database, (11, 15), "LevelMenu/Details/TxtATSPValueChange", "ATSP",parent_object=selected_turret,variable_name="atsp_change"))

    else:
        for x in wave_menu['WaveMenu/Details'].members_group.sprites():
            x.remove(wave_menu['WaveMenu/Details'].members_group)
            #wave_menu['WaveMenu/Details'].members_group.remove(x)
        to_remove=[]
        for x in wave_menu:
            if x[:17]=="WaveMenu/Details/": to_remove.append(x)
        for xx in to_remove:
            wave_menu.pop(xx)


def create_victory_menu(database):
    LM = {}
    victory_menu = pygame.sprite.Group()
    victory_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                             (database["resolution_in_tiles_percent_xy"][7][0],
                              database["resolution_in_tiles_percent_xy"][10][1]),
                             (database["resolution_in_tiles_percent_xy"][11][0],
                              database["resolution_in_tiles_percent_xy"][10][1]), "VictoryMenu", "Victory",
                             tile_size_xy=database["quadrupal_tile_size_xy"], draggable=False))
    LM['VictoryMenu'] = get_member_by_name(victory_menu.sprites(), "VictoryMenu")

    LM['VictoryMenu/Text0'] = LM['VictoryMenu'].add(
        MenuText(LM['VictoryMenu'].px_start_xy, database, (2, 5), "VictoryMenu/Text0",
                 "Congratulations! Here are your prices:"))

    LM['VictoryMenu/gridPrices'] = LM['VictoryMenu'].add(
        GuiGrid(LM['VictoryMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][4][0], 2), (4, 1),
                "VictoryMenu", tile_size_xy=database["quadrupal_tile_size_xy"]))

    lvl=database["current_level"]
    for i in range(len(database["world_prices_and_enemies"]["prices"][lvl-1])):

        if database["world_prices_and_enemies"]["prices"][lvl-1][i][:6] != "random":
            LM['VictoryMenu/gridPrices/ItemPrice'+str(i)] = LM[
                'VictoryMenu/gridPrices'].add(
                ItemMenu(LM['VictoryMenu/gridPrices'].px_start_xy, database, (i, 0),
                         'VictoryMenu/gridPrices' + str(i),
                         tile_size_xy=database["quadrupal_tile_size_xy"],
                         item_name=database["world_prices_and_enemies"]["prices"][lvl-1][i],
                         parent_grid=LM['VictoryMenu/gridPrices'], draggable=False))

        if database["world_prices_and_enemies"]["prices"][lvl-1][i] =="random_turret":

            tur = None
            while tur is None and len(database["available_turrets"])<available_turrets:
                tur = available_turrets[randint(0, len(available_turrets)-1)]
                if tur in database["available_turrets"]:
                    tur=None
            database["world_prices_and_enemies"]["prices"][lvl-1][i]=tur

            LM['VictoryMenu/gridPrices/ItemPrice'+str(i)] = LM[
            'VictoryMenu/gridPrices'].add(
            ItemMenu(LM['VictoryMenu/gridPrices'].px_start_xy, database, (i, 0),
                     'VictoryMenu/gridPrices' + str(i),
                     tile_size_xy=database["quadrupal_tile_size_xy"],
                     item_name=database["world_prices_and_enemies"]["prices"][lvl-1][i],
                     parent_grid=LM['VictoryMenu/gridPrices'], draggable=False))


    LM['VictoryMenu/button0'] = LM['VictoryMenu'].add(
        MenuButton(LM['VictoryMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][15][0], database["resolution_in_tiles_percent_xy"][25][1]),
                   (database["resolution_in_tiles_percent_xy"][16][0] * 4, 16), "VictoryMenu/button0",
                   text="OK", color=3, action="start_new_game"))

    return victory_menu, LM



def create_defeat_menu(database):
    LM = {}
    defeat_menu = pygame.sprite.Group()
    defeat_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                             (database["resolution_in_tiles_percent_xy"][7][0],
                              database["resolution_in_tiles_percent_xy"][10][1]),
                             (database["resolution_in_tiles_percent_xy"][11][0],
                              database["resolution_in_tiles_percent_xy"][10][1]), "DefeatMenu", "Defeat",
                             tile_size_xy=database["quadrupal_tile_size_xy"], draggable=False))
    LM['DefeatMenu'] = get_member_by_name(defeat_menu.sprites(), "DefeatMenu")

    LM['DefeatMenu/Text0'] = LM['DefeatMenu'].add(
        MenuText(LM['DefeatMenu'].px_start_xy, database, (2, 5), "DefeatMenu/Text0",
                 "You have been defeated! Try harder next time"))


    LM['DefeatMenu/button0'] = LM['DefeatMenu'].add(
        MenuButton(LM['DefeatMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][15][0], database["resolution_in_tiles_percent_xy"][25][1]),
                   (database["resolution_in_tiles_percent_xy"][16][0] * 4, 16), "DefeatMenu/button0",
                   text="OK", color=3, action="mainmenu"))

    return defeat_menu, LM


def create_game_victory_menu(database):
    LM = {}
    defeat_menu = pygame.sprite.Group()
    defeat_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                             (database["resolution_in_tiles_percent_xy"][7][0],
                              database["resolution_in_tiles_percent_xy"][10][1]),
                             (database["resolution_in_tiles_percent_xy"][11][0],
                              database["resolution_in_tiles_percent_xy"][10][1]), "GameVictoryMenu", "Victory",
                             tile_size_xy=database["quadrupal_tile_size_xy"], draggable=False))
    LM['GameVictoryMenu'] = get_member_by_name(defeat_menu.sprites(), "GameVictoryMenu")

    LM['GameVictoryMenu/Text0'] = LM['GameVictoryMenu'].add(
        MenuText(LM['GameVictoryMenu'].px_start_xy, database, (2, 5), "GameVictoryMenu/Text0",
                 "Congratulations! You have won the game"))


    LM['GameVictoryMenu/button0'] = LM['GameVictoryMenu'].add(
        MenuButton(LM['GameVictoryMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][15][0], database["resolution_in_tiles_percent_xy"][25][1]),
                   (database["resolution_in_tiles_percent_xy"][16][0] * 4, 16), "GameVictoryMenu/button0",
                   text="OK", color=3, action="mainmenu"))

    return defeat_menu, LM

def create_shop_menu(database):
    LM = {}
    shop_menu = pygame.sprite.Group()
    shop_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                             (database["resolution_in_tiles_percent_xy"][7][0],
                              database["resolution_in_tiles_percent_xy"][10][1]),
                             (database["resolution_in_tiles_percent_xy"][11][0],
                              database["resolution_in_tiles_percent_xy"][10][1]), "ShopMenu", "Upgrade",
                             tile_size_xy=database["quadrupal_tile_size_xy"], draggable=False))
    LM['ShopMenu'] = get_member_by_name(shop_menu.sprites(), "ShopMenu")

    LM['ShopMenu/Title1']=LM['ShopMenu'].add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                             (database["resolution_in_tiles_percent_xy"][25][0],
                              database["resolution_in_tiles_percent_xy"][5][1]),
                             (database["resolution_in_tiles_percent_xy"][7][0],
                              database["resolution_in_tiles_percent_xy"][7][1]), "ShopMenu/Title1", "Gems",
                             tile_size_xy=database["double_tile_size_xy"], draggable=False))

    LM['ShopMenu/Title1/TextGems'] = LM['ShopMenu/Title1'].add(
        MenuText(LM['ShopMenu'].px_start_xy, database, (2, 2), "ShopMenu/Title1/TextGems",
                 "a"))

    LM['ShopMenu/Title1/TextGems_change']=LM['ShopMenu/Title1'].add(MenuText(LM['ShopMenu'].px_start_xy, database, (4, 2), "ShopMenu/Title1/TextGems_change",
                 "a",variable_name="gems_change"))


    LM['ShopMenu/Text0'] = LM['ShopMenu'].add(
        MenuText(LM['ShopMenu'].px_start_xy, database, (2, 5), "ShopMenu/Text0",
                 "What would you like to buy?"))

    LM['ShopMenu/button1'] = LM['ShopMenu'].add(
        MenuButton(LM['ShopMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][5][0], database["resolution_in_tiles_percent_xy"][15][1]),
                   (database["resolution_in_tiles_percent_xy"][16][0] * 4, 16), "ShopMenu/button1",
                   text="Starting gold + 50", color=3, action="upgrade_gold"))
    LM['ShopMenu/button2'] = LM['ShopMenu'].add(
        MenuButton(LM['ShopMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][24][0], database["resolution_in_tiles_percent_xy"][15][1]),
                   (database["resolution_in_tiles_percent_xy"][16][0] * 4, 16), "ShopMenu/button2",
                   text="Lives + 2", color=3, action="upgrade_lives"))

    LM['ShopMenu/button0'] = LM['ShopMenu'].add(
        MenuButton(LM['ShopMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][15][0], database["resolution_in_tiles_percent_xy"][25][1]),
                   (database["resolution_in_tiles_percent_xy"][16][0] * 4, 16), "ShopMenu/button0",
                   text="OK", color=3, action="start_new_game"))

    return shop_menu, LM


def create_armory_menu(database):
    LM = {}
    armory_menu = pygame.sprite.Group()
    armory_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                             (database["resolution_in_tiles_percent_xy"][7][0],
                              database["resolution_in_tiles_percent_xy"][10][1]),
                             (database["resolution_in_tiles_percent_xy"][11][0],
                              database["resolution_in_tiles_percent_xy"][15][1]), "ArmoryMenu", "Armory",
                             tile_size_xy=database["quadrupal_tile_size_xy"], draggable=False))
    LM['ArmoryMenu'] = get_member_by_name(armory_menu.sprites(), "ArmoryMenu")

    LM['ArmoryMenu/Title1'] = LM['ArmoryMenu'].add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                                                         (database["resolution_in_tiles_percent_xy"][25][0],
                                                          database["resolution_in_tiles_percent_xy"][5][1]),
                                                         (database["resolution_in_tiles_percent_xy"][7][0],
                                                          database["resolution_in_tiles_percent_xy"][7][1]),
                                                         "ArmoryMenu/Title1", "Gems",
                                                         tile_size_xy=database["double_tile_size_xy"], draggable=False))

    LM['ArmoryMenu/Title1/TextGems'] = LM['ArmoryMenu/Title1'].add(
        MenuText(LM['ArmoryMenu'].px_start_xy, database, (2, 2), "ArmoryMenu/Title1/TextGems",
                 "a"))

    LM['ArmoryMenu/Title1/TextGems_change'] = LM['ArmoryMenu/Title1'].add(
        MenuText(LM['ArmoryMenu'].px_start_xy, database, (4, 2), "ArmoryMenu/Title1/TextGems_change",
                 "a", variable_name="gems_change"))


    LM['ArmoryMenu/Text0'] = LM['ArmoryMenu'].add(
        MenuText(LM['ArmoryMenu'].px_start_xy, database, (2, 5), "ArmoryMenu/Text0",
                 "What would you like to upgrade?"))

    for index in range(len(database["available_turrets"])):
        LM['ArmoryMenu/grid'+str(index)] =LM['ArmoryMenu'].add(GuiGrid(LM['ArmoryMenu'].px_start_xy, database, (0.5+(index*2.75), 2),(1,1), "ArmoryMenu/grid"+str(index),tile_size_xy=database["quadrupal_tile_size_xy"]))

        LM['ArmoryMenu/grid' + str(index)+"/Item"] = LM['ArmoryMenu/grid' + str(index)].add(ItemMenu(LM['ArmoryMenu/grid' + str(index)].px_start_xy, database, (0, 0),  'ArmoryMenu/grid' + str(index)+"/Item",tile_size_xy=database["quadrupal_tile_size_xy"],item_name=database["available_turrets"][index],parent_grid=LM['ArmoryMenu/grid' + str(index)]))

        LM['ArmoryMenu/grid' + str(index) +"ButtonDMG"]=LM['ArmoryMenu/grid'+str(index)].add(MenuButton(LM['ArmoryMenu/grid'+str(index)].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][4][0], database["resolution_in_tiles_percent_xy"][0][1]),
                   (database["resolution_in_tiles_percent_xy"][5][0] * 4, 7), 'ArmoryMenu/grid' + str(index) +"ButtonDMG",
                   text="DMG", color=3, action="armory_upgrade_turret"))
        LM['ArmoryMenu/grid' + str(index) +"ButtonRange"]=LM['ArmoryMenu/grid'+str(index)].add(MenuButton(LM['ArmoryMenu/grid'+str(index)].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][4][0], database["resolution_in_tiles_percent_xy"][4][1]),
                   (database["resolution_in_tiles_percent_xy"][5][0] * 4, 7), 'ArmoryMenu/grid' + str(index) +"ButtonRange",
                   text="Range", color=3, action="armory_upgrade_turret"))
        LM['ArmoryMenu/grid' + str(index) +"ButtonATSP"]=LM['ArmoryMenu/grid'+str(index)].add(MenuButton(LM['ArmoryMenu/grid'+str(index)].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][4][0], database["resolution_in_tiles_percent_xy"][8][1]),
                   (database["resolution_in_tiles_percent_xy"][5][0] * 4, 7), 'ArmoryMenu/grid' + str(index) +"ButtonATSP",
                   text="ATSP", color=3, action="armory_upgrade_turret"))

        LM['ArmoryMenu/grid' + str(index) +"/TextDMG"] = LM['ArmoryMenu/grid' + str(index)].add(
            MenuText(LM['ArmoryMenu/grid' + str(index)].px_start_xy, database, (0, 6), 'ArmoryMenu/grid' + str(index) +"/TextDMG",
                     "DMG: 1000"))
        LM['ArmoryMenu/grid' + str(index) +"/TextDMG_change"] = LM['ArmoryMenu/grid' + str(index)].add(
            MenuText(LM['ArmoryMenu/grid' + str(index)].px_start_xy, database, (7, 6), 'ArmoryMenu/grid' + str(index) +"/TextDMG_change",
                     "+100"))

        LM['ArmoryMenu/grid' + str(index) +"/TextRange"] = LM['ArmoryMenu/grid' + str(index)].add(
            MenuText(LM['ArmoryMenu/grid' + str(index)].px_start_xy, database, (0, 8), 'ArmoryMenu/grid' + str(index) +"/TextRange",
                     "Range: 1000"))
        LM['ArmoryMenu/grid' + str(index) +"/TextRange_change"] = LM['ArmoryMenu/grid' + str(index)].add(
            MenuText(LM['ArmoryMenu/grid' + str(index)].px_start_xy, database, (7, 8), 'ArmoryMenu/grid' + str(index) +"/TextRange_change",
                     "+100"))

        LM['ArmoryMenu/grid' + str(index) +"/TextATSP"] = LM['ArmoryMenu/grid' + str(index)].add(
            MenuText(LM['ArmoryMenu/grid' + str(index)].px_start_xy, database, (0, 10), 'ArmoryMenu/grid' + str(index) +"/TextATSP",
                     "ATSP: 1000"))
        LM['ArmoryMenu/grid' + str(index) +"/TextATSP_change"] = LM['ArmoryMenu/grid' + str(index)].add(
            MenuText(LM['ArmoryMenu/grid' + str(index)].px_start_xy, database, (7, 10), 'ArmoryMenu/grid' + str(index) +"/TextATSP_change",
                     "+ 100"))


    LM['ArmoryMenu/button0'] = LM['ArmoryMenu'].add(
        MenuButton(LM['ArmoryMenu'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][15][0], database["resolution_in_tiles_percent_xy"][45][1]),
                   (database["resolution_in_tiles_percent_xy"][16][0] * 4, 16), "ArmoryMenu/button0",
                   text="OK", color=3, action="start_new_game"))

    return armory_menu, LM







projectile_init_database={
    "arrow":{
        "dmg_type":"single",
        "target_type":"mob",
        "sprite":"arrow_sprite",
        "projectile_speed":10
    },
    "bomb": {
        "dmg_type": "splash",
        "target_type":"ground",
        "sprite":"bomb_sprite",
        "scale":"quadrupal_tile_size_xy",
        "projectile_speed":5
    },
"rock": {
        "dmg_type": "single",
        "target_type":"mob",
        "sprite":"bomb_sprite",
        "scale":"quadrupal_tile_size_xy",
        "projectile_speed":5
    }


}

turret_init_database={
    "archer":
                  {"dmg":15,
                 "dmg_upgrade":5,
                 "dmg_change": "",
                 "atsp": 2000,
                 "atsp_upgrade":-50,
                 "atsp_change":"",
                 "range": 300,
                 "range_upgrade":10,
                 "range_change":"",
                 "food_price":10,
                 "buy_price":50,
                 "sell_price":50,
                 "upgrade_price":25,
                 "target_type":"most_hp",
                 "projectile_type":"arrow",
"projectile_speed":10,
                 "sprite_name":"archer_sprite"
        },
    "catapult":
        {"dmg": 50,
         "dmg_upgrade": 10,
         "dmg_change": "",
         "atsp": 3000,
         "atsp_upgrade": -200,
         "atsp_change": "",
         "range": 150,
         "range_upgrade": 10,
         "range_change": "",
         "food_price":30,
         "buy_price": 150,
         "sell_price": 75,
         "upgrade_price": 50,
         "target_type": "most_hp",
         "projectile_type":"bomb",
    "projectile_speed":5,
         "sprite_name": "catapult_sprite"
         },
    "cyclop":
        {"dmg": 50,
         "dmg_upgrade": 10,
         "dmg_change": "",
         "atsp": 3000,
         "atsp_upgrade": -250,
         "atsp_change": "",
         "range": 400,
         "range_upgrade": 10,
         "range_change": "",
         "buy_price": 100,
         "food_price":20,
         "sell_price": 75,
         "upgrade_price": 50,
         "target_type": "most_hp",
         "projectile_type": "rock",
         "projectile_speed": 5,
         "sprite_name": "cyclop_sprite"
         },

                 }


levels_dict={
 "umap":{
  "filename": "road_map1_40x28.png"
 },
 "umapc": {
  "filename": "road_mapc_40x28.png"
 },
 "zigzag":{
  "filename": "road_map2_40x28.png"
 },
 "zigzagc": {
  "filename": "road_map2c_40x28.png"
 },
 "bulb": {
  "filename": "road_mapBULBc_40x28.png"
 },
 "cos": {
  "filename": "road_mapCOSc_40x28.png"
 },
 "long": {
  "filename": "road_mapLONGc_40x28.png"
 },
 "zmap": {
  "filename": "road_mapZc_40x28.png"
 }

}


map1=[
 ["","wsd","wsad","wsa","","","","","","","","","","","wsd","wsad","wsa",""],
 ["","wsd","wsad","wsa","","","","","","","","","","","wsd","wsad","wsa",""],
 ["","wsd","wsad","wsa","","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["","wsd","wsad","Xwd","sad","sad","sad","sad","sad","sad","sad","sad","sad","sad","Xwa","wsad","wsa","",""],
 ["","wsd","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsa",""],
 ["","wd","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wa","",""],
]
road_tiles = {
"sd":"road_1.png",
"sad":"road_2.png",
"sa":"road_3.png",
"wsd":"road_4.png",
"wsad":"road_5.png",
"wsa":"road_6.png",
"wd":"road_7.png",
"wad":"road_8.png",
"wa":"road_9.png",
"Xsd":"road_10.png",
"Xsa":"road_11.png",
"Xwd":"road_12.png",
"Xwa":"road_13.png"
}
road_tiles_old = {
"sd":"img/road/road_1.png",
"sad":"img/road/road_2.png",
"sa":"img/road/road_3.png",
"wsd":"img/road/road_4.png",
"wsad":"img/road/road_5.png",
"wsa":"img/road/road_6.png",
"wd":"img/road/road_7.png",
"wad":"img/road/road_8.png",
"wa":"img/road/road_9.png",
"Xsd":"img/road/road_10.png",
"Xsa":"img/road/road_11.png",
"Xwd":"img/road/road_12.png",
"Xwa":"img/road/road_13.png"
}

mob_path1_data={
 'START' : [64,20],
 'POINTS': [[64,476],[476,476],[476,0]],
 'FINISH' : [476,0]
}
mob_path2_data={
 'START': [20, 20],
 'POINTS': [[20, 320], [400, 320], [400, 120],[300,120],[300,220],[500,220],[500,20]],
 'FINISH': [500, 20]
}
animation_sprites={}
animation_sprites["random_turret_sprite"] = {
'IDLE': {
'path': "img/items/random_turret.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':6,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}}
animation_sprites["victory_sprite"] = {
'IDLE': {
'path': "img/items/victory.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':6,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}}
animation_sprites["random_item_sprite"] = {
'IDLE': {
'path': "img/items/random_item.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':6,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}}
animation_sprites["gem_sprite"] = {
'IDLE': {
'path': "img/items/gem.png",
'frame_window_width':16,
'frame_window_height':16,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':6,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}}
animation_sprites["chicken_sprite"] = {
'IDLE': {
'path': "img/items/chicken.png",
'frame_window_width':16,
'frame_window_height':16,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':6,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}}
animation_sprites["steak_sprite"] = {
'IDLE': {
'path': "img/items/steak.png",
'frame_window_width':16,
'frame_window_height':16,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':6,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}}

animation_sprites["bomb_sprite"] = {
'IDLE': {
'path': "img/bomg.png",
'frame_window_width':32,
'frame_window_height':16,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':6,
'init_rotation':90,
'start_x':0,
'start_y':0,
'frames_count':5,
'img_per_row_or_col':5,
'color_key':(0,0,0)
},
'HIT': {
'path': "img/bomb_explode.png",
'frame_window_width':16,
'frame_window_height':16,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(0,0,0)
}
}
animation_sprites["arrow_sprite"] = {
'IDLE': {
'path': "img/arrow3.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':1,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}
}
animation_sprites["spider_sprite"] = {

'IDLE': {
'path': "img/mobs/spider/spider_down.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':4,
'color_key':(255,255,255)
},
'WALK_DOWN': {
'path': "img/mobs/spider/spider_down.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(255,255,255)
},
'WALK_UP': {
'path': "img/mobs/spider/spider_up.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(255,255,255)
},
'WALK_LEFT': {
'path': "img/mobs/spider/spider_left.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(255,255,255)
},
'WALK_RIGHT': {
'path': "img/mobs/spider/spider_right.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(255,255,255)
}}

animation_sprites["eye_sprite"] = {
'IDLE': {
'path': "img/mobs/eye/eye_down.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':4,
'color_key':(255,255,255)
},
'WALK_DOWN': {
'path': "img/mobs/eye/eye_down.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':9,
'img_per_row_or_col':9,
'color_key':(255,255,255)
},
'WALK_UP': {
'path': "img/mobs/eye/eye_up.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':9,
'img_per_row_or_col':9,
'color_key':(255,255,255)
},
'WALK_LEFT': {
'path': "img/mobs/eye/eye_left.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':9,
'img_per_row_or_col':9,
'color_key':(255,255,255)
},
'WALK_RIGHT': {
'path': "img/mobs/eye/eye_right.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':9,
'img_per_row_or_col':9,
'color_key':(255,255,255)
}}
### GOBLIN
animation_sprites["goblin_sprite"] = {
'WALK_DOWN': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
},
'IDLE': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
},
'WALK_LEFT': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':64,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
 },
'WALK_RIGHT': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':128,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
},
'WALK_UP': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':192,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
}
}
### /GOBLIN
### SKELETON
animation_sprites["skeleton_sprite"] = {
'IDLE': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
'WALK_DOWN': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':0,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
'WALK_LEFT': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':64,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
'WALK_RIGHT': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':128,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
'WALK_UP': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':192,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
}

### /SKELETON

animation_sprites["catapult_sprite"]={
 'FIRE':{
'path': "img/Turrets/catapult/catapult.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'fire_at_frame':4,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':7,
'img_per_row_or_col':7,
'color_key':(0,0,0)
},
'IDLE': {
'path': "img/Turrets/catapult/catapult.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':5,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}
}

animation_sprites["cyclop_sprite"]={
 'FIRE':{
'path': "img/Turrets/cyclop/cyclop.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'fire_at_frame':6,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':7,
'img_per_row_or_col':7,
'color_key':(0,0,0)
},
'IDLE': {
'path': "img/Turrets/cyclop/cyclop.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':5,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}
}
### ARCHER
animation_sprites["archer_sprite"]={
'WALK_RIGHT': {
'path': "img/anim.png",
'frame_window_width':73,
'frame_window_height':73,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':129,
'start_y':185,
'frames_count':10,
'img_per_row_or_col':5,
'color_key':(79,143,186)
},
'FIRE': {
'path': "img/anim.png",
'frame_window_width':73,
'frame_window_height':73,
'animation_orientation':"horizontal",
'border':1,
'fire_at_frame':10,
'anim_fps':20,
'start_x':129,
'start_y':406,
'frames_count':17,
'img_per_row_or_col':5,
'color_key':(79,143,186)
},
'IDLE': {
'path': "img/anim.png",
'frame_window_width':73,
'frame_window_height':73,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':5,
'start_x':129,
'start_y':111,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(79,143,186)
}
}


pygame.init()
pygame.display.set_caption("Marek")
clock = pygame.time.Clock()
last_update_time = pygame.time.get_ticks()

fnt_list=["arial","comicsansms"]
fnt_sizes=tab=get_fonts_sizes(fnt_list,list(range(6,30)))

#resolution_xy = (1600, 900)
#resolution_xy = (1400, 800)
resolution_xy = (1366,768)
#resolution_xy = (800, 600)
#resolution_xy = (1066, 600)
#resolution_xy = (426 , 240)
#640 x 360 pixels
#1280 x 720 pixels
#tile_size_xy = (16, 16)
resolution_in_tiles=(100,56)

tile_size_xy= (floor(resolution_xy[0]/resolution_in_tiles[0]), floor(resolution_xy[1]/resolution_in_tiles[1]))
resolution_in_tiles_percent_xy = {}
for p in range(150):
    resolution_in_tiles_percent_xy[p] = (floor(resolution_in_tiles[0] * p / 100),
                                         floor(resolution_in_tiles[1] * p / 100))
init_gold=200
init_food=2

init_gems=0
init_lives=5
database = {
    "fps": 60,
    "resolution_xy": resolution_xy,
    "tile_size_xy": tile_size_xy,
    "double_tile_size_xy": (tile_size_xy[0]*2, tile_size_xy[1]*2),
    "triple_tile_size_xy": (tile_size_xy[0]*3, tile_size_xy[1]*3),
    "quadrupal_tile_size_xy": (tile_size_xy[0]*4, tile_size_xy[1]*4),
    "half_tile_size_xy":(floor(tile_size_xy[0]/2), floor(tile_size_xy[1]/2)),
    #"resolution_in_tiles": (floor(resolution_xy[0] / tile_size_xy[0]), floor(resolution_xy[1] / tile_size_xy[1])),
    "resolution_in_tiles":resolution_in_tiles,
    "resolution_in_tiles_percent_xy":resolution_in_tiles_percent_xy,
    "lives": init_lives,
    "init_lives": init_lives,
    "gold": init_gold,
    "init_gold": init_gold,
    "food": init_food,
    "food_change":0,
    "gems_change":0,
    "gems": init_gems,
    "armory_change":(),
    "wave_shop_items":[],
    "available_turrets":["archer"],
    #"available_turrets":["archer","cyclop","catapult"],
    "gold_change":"",
    "wave_number": 0,

    "font_sizes":fnt_sizes,
    "wave_menu_width_pt": 20,
    "building_allowed_map":{}
}


print(database)
#screen = pygame.display.set_mode(database["resolution_xy"], pygame.FULLSCREEN)
screen = pygame.display.set_mode(database["resolution_xy"])

All_menus_groups_ordered=[]

inv_menu_index=0
#All_menus_groups_ordered.append(create_inventory_menu(database))
#All_menus_groups_ordered.append(create_test_menu(database,inv_menu_index))
#All_menus_groups_ordered.append(create_chest_menu(database))
All_menus_groups_ordered.append(create_main_menu(database))

###MOBS
mobs = pygame.sprite.Group()
wave_mob=[]
#mobs.add(MobSprite(goblin_sprite, database["fps"], mob_path_1.start[0] + pth_off[0], mob_path_1.start[1] + pth_off[1],mob_path_1, 2, path_offset=pth_off,init_hp=30))



### TURRETS
turret_group= pygame.sprite.Group()

#archer_sprite=AnimationData(archer_sprite)
#catapult_sprite=AnimationData(catapult_sprite)



selected_turret=None
background=None

#turret_sprites= {"cyclop_sprite": AnimationData(cyclop_sprite),"catapult_sprite": AnimationData(catapult_sprite), "archer_sprite": AnimationData(archer_sprite)}

projectiles=pygame.sprite.Group()

#anim_data={"arrow":AnimationData(arrow_sprite),"bomb":AnimationData(bomb_sprite),"rock":AnimationData(bomb_sprite)}
#arrow_sprite=AnimationData(arrow_sprite)
#bomb_sprite=AnimationData(bomb_sprite)

is_game_on=False

async def main():
    global is_game_on
    global turret_group
    global mobs
    global projectiles
    global selected_turret
    global All_menus_groups_ordered
    global last_update_time

    while True:


        screen.fill("yellow")
        if is_game_on and background is not None:
            screen.blit(background,(0,0))



        ### MAP / VICTORY / STATS
        if is_game_on:
            print_road(screen, map, road,database["double_tile_size_xy"])

            wave_menu['WaveMenu/Stats/Lives'].update(txt="Lives: "+str(database["lives"]))
            wave_menu['WaveMenu/Stats/Gold'].update(txt="Gold: " + str(database["gold"]))
            wave_menu['WaveMenu/Stats/GoldChange'].update(txt=str(database["gold_change"]))
            database["gold_change"]=""

            wave_menu['WaveMenu/Info/Debug1'].update(txt=str(pygame.mouse.get_pos()))

            ### DEFEAT
            #if True:
            if database['lives']<1:
                is_game_on = False
                All_menus_groups_ordered = []
                turret_group = pygame.sprite.Group()
                All_menus_groups_ordered.append(create_defeat_menu(database))
                projectiles = pygame.sprite.Group()
                mobs = pygame.sprite.Group()
                selected_turret=None

            ### VICTORY
            #if True:
            if len(levels_list[database["current_level"]].waves)<= database["wave_number"] and len(wave_mob)==0 and len(mobs)==0 and database['lives']>-1:
                is_game_on=False
                All_menus_groups_ordered = []
                turret_group=pygame.sprite.Group()
                if "victory" not in database["world_prices_and_enemies"]["prices"][database["current_level"]-1]:
                    All_menus_groups_ordered.append(create_victory_menu(database))
                else:
                    All_menus_groups_ordered.append(create_game_victory_menu(database))
                projectiles=pygame.sprite.Group()
                mobs = pygame.sprite.Group()
                grand_prices(database,database["world_prices_and_enemies"]["prices"][database["current_level"]-1])
                selected_turret = None

            ### TURRETS
        if turret_group!=[]:
            turret_group.update(mobs, database)
            turret_group.draw(screen)



        ### MOBS UPDATE N DRAW
        if mobs is not []:
            mobs.update()
            mobs_sprite_list = mobs.sprites()
            mobs_sprite_list.sort(key=sort_sprites)
            for mob in mobs_sprite_list:
                screen.blit(mob.image, mob.rect)


        ## SPAWN MOBS
        if is_game_on:
            mobs,wave_mob=spawn_mobs(wave_mob,mobs,database,mob_path)

        ### TERMINATE MOBS
        for mob in mobs:
            if mob.reached_finish:
                mobs.remove(mob)
                database['lives']-=1
            if mob.hp<=0:
                mobs.remove(mob)
                database['gold']+=mob_database[mob.data.name]["award"]

        ### PROJECTILES
        for projectile in projectiles.sprites():
            if projectile.remove_me: projectiles.remove(projectile)
        projectiles.update()
        projectiles.draw(screen)

        ### TURRET RANGE
        if selected_turret is not None:
            pygame.draw.circle(screen, "white", selected_turret.rect.center, selected_turret.db["range"],1)


        ### MENUS
        if All_menus_groups_ordered != []:

            for group in All_menus_groups_ordered:
                group[0].update(allowed_map=database["building_allowed_map"],database=database)
                if "LevelMenu/Title0/Title2/TextFood" in group[1].keys():
                    update_shop_details(menu=group[1],database=database)
                if "ShopMenu/Title1/TextGems" in group[1].keys():
                    update_shop_mm_details(menu=group[1],database=database)
                    database["food_change"] = 0
                    database["gems_change"] = 0
                if "ArmoryMenu/Title1/TextGems" in group[1].keys():
                    update_armory_mm_details(menu=group[1],database=database)
                    database["food_change"] = 0
                    database["gems_change"] = 0

                    database["armory_change"]=()




            groups, MMs = zip(*All_menus_groups_ordered)
            MMs=list(MMs)
            detect_menu_mouse_hoover(MMs)

            for group in groups:
                for mm in group.sprites(): mm.draw(screen)

            ### VERY UGLY HACK TO DRAW DRAGGED ITEM ON TOP OF OTHER MENUS   BUT WORKS :d
            for mm in MMs:
                for mmm in mm:
                    if type(mm[mmm])==ItemMenu:
                        mm[mmm].draw(screen)


        ### DEBUG PRINT ALLOWED MAP
        # if database["building_allowed_map"] != {}:
        #     for x in range(database["resolution_xy"][0]):
        #         for y in range(database["resolution_xy"][1]):
        #             if database["building_allowed_map"][x,y]: pygame.draw.rect(screen,(255,255,255),(x,y,1,1))


        ### EVENTS
        ev=[]
        ### CZYZBY PODLACZONY JOY ROBIŁ PROBLEMY ???
        # try:
        #     ev=pygame.event.get()
        # except Exception as e: print(e)
        # finally:
        #     pass
        ev = pygame.event.get()
        for events in ev:
            #print(events)
            ###### MOUSE DOWN
            if events.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                colliding_objects=find_colliding_objects(mouse_pos,MMs,turret_group.sprites())


                if selected_turret is not None and (colliding_objects == [] or MenuTitle not in [type(a) for a in colliding_objects]):

                    selected_turret.bordered=False
                    create_wave_turret_details(wave_menu,selected_turret,database,destroy=True)
                    selected_turret=None

                if events.button == 1:
                    handle_LMB_down(colliding_objects,mouse_pos)

                    bring_root_to_front(colliding_objects, All_menus_groups_ordered)

                if events.button == 3:
                    handle_RMB_down(colliding_objects,mouse_pos)
                    bring_root_to_front(colliding_objects, All_menus_groups_ordered)
            ###### MOUSE UP
            if events.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                colliding_objects = find_colliding_objects(mouse_pos, MMs,turret_group.sprites())
                if events.button == 1:
                    handle_LMB_up(colliding_objects,mouse_pos)
                if events.button == 3:
                    handle_RMB_up(colliding_objects,mouse_pos)


            ###### CALL ACTIONS
            if events.type == pygame.USEREVENT:
                if events.dict["action"]=="close_root_menu":
                    for i in range(len(All_menus_groups_ordered)):
                        if events.dict["button_name"] in All_menus_groups_ordered[i][1].keys():
                            All_menus_groups_ordered[i][0].empty()
                            All_menus_groups_ordered.pop(i)


                # if events.dict["action"] == "create_test_menu":
                #     inv_menu_index+=1
                #     All_menus_groups_ordered.append(create_test_menu(database, inv_menu_index))

                if events.dict["action"]=="move_item_from_grid_to_grid":
                    move_item_from_grid_to_grid(events.dict,All_menus_groups_ordered,database)

                if events.dict["action"]=="quit_game":
                    pygame.quit()
                    exit()

                if events.dict["action"]=="start_new_game":
                    All_menus_groups_ordered= []
                    All_menus_groups_ordered.append(create_world_menu(database))
                    levels_list = wave_generator(database["world_prices_and_enemies"]["enemies"])

                if events.dict["action"]=="mainmenu":
                    All_menus_groups_ordered = []
                    All_menus_groups_ordered.append(create_main_menu(database))
                    database["food"] = init_food
                    database["gems"] = init_gems


                if events.dict["action"]=="open_shop":
                    All_menus_groups_ordered = []
                    All_menus_groups_ordered.append(create_shop_menu(database))

                if events.dict["action"]=="open_armory":
                    All_menus_groups_ordered = []
                    All_menus_groups_ordered.append(create_armory_menu(database))

                if events.dict["action"]=="start_battle":
                    database["wave_shop_items"]=[]
                    database["gold"]=database["init_gold"]
                    database["lives"] = database["init_lives"]

                    subtract_costs(database,All_menus_groups_ordered[0][1]['LevelMenu/Title0/Title0/gridActive'])

                    for item in All_menus_groups_ordered[0][1]['LevelMenu/Title0/Title0/gridActive'].members_group.sprites():
                        database["wave_shop_items"].append(item.item_name)

                    All_menus_groups_ordered = []
                    is_game_on=True

                    database["current_level"]=int(events.dict["button_name"][-1])

                    map, road, building_allowed_map, mob_path, background = load_level(levels_dict[levels_list[database["current_level"]].road_map]["filename"],road_tiles, database)

                    database["building_allowed_map"]=building_allowed_map
                    tmp=create_wave_menu(database)
                    All_menus_groups_ordered.append(tmp)
                    wave_menu=tmp[1]


                    database["wave_number"]=1
                    wave_mob = generate_wave2(database,levels_list)
                    #wave_mob = generate_wave(levels_list[database["current_level"]].waves(database["wave_number"]).number, AnimationData(levels_list[database["current_level"]].waves(database["wave_number"]).mob), pygame.time.get_ticks(),pygame.time.get_ticks() + (10 * 1000))

                    wave_menu['WaveMenu/Stats/Gold'].update(txt="Gold: " + str(database["gold"]))
                    wave_menu['WaveMenu/Stats/Wave'].update(txt="Wave: " + str(database["wave_number"]))

                if events.dict["action"]=="next_wave":
                    if database["wave_number"] < len(levels_list[database["current_level"]].waves):
                        database["wave_number"] += 1
                        wave_menu['WaveMenu/Stats/Wave'].update(txt="Wave: " + str(database["wave_number"]))

                        wave_mob+= generate_wave2(database,levels_list)
                            #wave_mob+= generate_wave(levels_list[database["current_level"]].waves(database["wave_number"]).number, AnimationData(levels_list[database["current_level"]].waves(database["wave_number"]).mob), pygame.time.get_ticks(),pygame.time.get_ticks() + (10 * 1000))




                if events.dict["action"]=="build_turret":
                    if database["gold"]>=events.dict["turret"].item.data["cost"]:
                        database["gold"]-=events.dict["turret"].item.data["cost"]
                        wave_menu['WaveMenu/Stats/Gold'].update(txt="Gold: " + str(database["gold"]))
                        turret_group.add(TurretSprite(AnimationData(animation_sprites[events.dict["turret"].item.data["sprite"]]), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], database["fps"],10, database["quadrupal_tile_size_xy"],events.dict["turret"].item.data["name"]))
                        for turret in turret_group.sprites():
                            building_allowed_map = exclude_from_build_map(building_allowed_map, turret.rect)

                if events.dict["action"] == "sell_turret":


                    database["gold"]+=events.dict["parent_object"].db["sell_price"]
                    events.dict["parent_object"].remove(turret_group)
                    building_allowed_map=exclude_from_build_map(building_allowed_map, turret.rect,include=True)
                    selected_turret=None

                if events.dict["action"] == "upgrade_turret":
                    if database["gold"] >= events.dict["parent_object"].db["upgrade_price"]:
                        events.dict["parent_object"].db["dmg"]+=events.dict["parent_object"].db["dmg_upgrade"]
                        events.dict["parent_object"].db["atsp"] += events.dict["parent_object"].db["atsp_upgrade"]
                        events.dict["parent_object"].db["range"] += events.dict["parent_object"].db["range_upgrade"]
                        database["gold"] -= events.dict["parent_object"].db["upgrade_price"]

                if events.dict["action"]=="shoot_projectile":
                    if len(mobs) > 0:
                        target = get_target((events.dict["sta"
                                                         "rt_xy"][0], events.dict["start_xy"][1]),
                                            events.dict["range"], events.dict["target_type"], mobs)

                        if target is not None:
                            if projectile_init_database[events.dict["projectile_type"]]["target_type"]=="mob":
                                projectile_sprite_name=projectile_init_database[events.dict["projectile_type"]]["sprite"]
                                projectiles.add(ProjectileSprite(AnimationData(animation_sprites[projectile_sprite_name]), database["fps"],events.dict["start_xy"][0], events.dict["start_xy"][1],events.dict["projectile_speed"], events.dict["dmg"], projectile_sprite_name,target_sprite=target,px_scale_to_xy=database["tile_size_xy"]))
                            else:
                                projectile_sprite_name = projectile_init_database[events.dict["projectile_type"]]["sprite"]
                                projectiles.add(ProjectileSprite(AnimationData(animation_sprites[projectile_sprite_name]), database["fps"],events.dict["start_xy"][0], events.dict["start_xy"][1],events.dict["projectile_speed"], events.dict["dmg"],events.dict["projectile_type"], target_xy=target.rect.center,px_scale_to_xy=database["tile_size_xy"]))

                if events.dict["action"]=="select_turret":
                    selected_turret=events.dict["turret"]
                    selected_turret.bordered=True
                    create_wave_turret_details(wave_menu,selected_turret,database)

                if events.dict["action"]=="set_gold_change":
                    database["gold_change"]=events.dict["gold_change"]
                if events.dict["action"]=="set_gems_change":
                    database["gems_change"]=events.dict["gems_change"]

                if events.dict["action"]=="set_armory_change":
                    but_name=events.dict["name"]
                    turret_index = int(but_name[15:16])
                    if but_name[-3:]=="DMG":
                        upgrade_what="dmg"
                        upgrade_value="dmg_upgrade"

                    if but_name[-3:]=="TSP":
                        upgrade_what="atsp"
                        upgrade_value="atsp_upgrade"
                    if but_name[-3:]=="nge":
                        upgrade_what="range"
                        upgrade_value="range_upgrade"
                    tmp=turret_init_database[database["available_turrets"][turret_index]][upgrade_value]

                    database["armory_change"]=(turret_index,upgrade_what,turret_init_database[database["available_turrets"][turret_index]][upgrade_value])



                if events.dict["action"] == "upgrade_lives":
                    database["init_lives"]+=2
                    database["gems"]-=1
                if events.dict["action"] == "upgrade_gold":
                    database["init_gold"]+=50
                    database["gems"]-=1

                #   TO TRZEBABY PRZENIESC DO FUNKCJI
                if events.dict["action"] == "armory_upgrade_turret":
                    turret_index=int(events.dict["button_name"][15:16])
                    if events.dict["button_name"][-3:]=="DMG":
                        upgrade_what="dmg"
                        upgrade_value="dmg_upgrade"

                    if events.dict["button_name"][-3:]=="TSP":
                        upgrade_what="atsp"
                        upgrade_value="atsp_upgrade"
                    if events.dict["button_name"][-3:]=="nge":
                        upgrade_what="range"
                        upgrade_value="range_upgrade"
                    tmp=turret_init_database[database["available_turrets"][turret_index]][upgrade_value]

                    turret_init_database[database["available_turrets"][turret_index]][upgrade_what]+=tmp
                    database["gems"]-=1



                if events.dict["action"] == "create_explosion":
                    #proj_type=events.dict["projectile_type"]
                    proj_type = projectile_init_database[events.dict["projectile_type"]]["sprite"]
                    projectiles.add(ExplosionSprite(AnimationData(animation_sprites[proj_type]),database,events.dict["explosion_xy"],database[projectile_init_database[events.dict["projectile_type"]]["scale"]]))
                    deal_splash_dmg(events.dict["explosion_xy"],events.dict["dmg"],events.dict["radius"],mobs_sprite_list)


            ##### QUIT
            if events.type == pygame.QUIT:
                pygame.quit()
                exit()
            if events.type == pygame.KEYDOWN:
                if events.key == K_ESCAPE:
                    pygame.quit()
                    exit()



        pygame.display.update()

        clock.tick(database["fps"])
        await asyncio.sleep(0)

        real_fps=pygame.time.get_ticks() - last_update_time
        last_update_time = pygame.time.get_ticks()
        pygame.display.set_caption(str(floor(1000/real_fps)))



asyncio.run(main())