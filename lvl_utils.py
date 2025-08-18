import pygame
from math import floor
from random import uniform

class MobPath:
    def __init__(self,start: list, finish: list ,points: list, offset: list = None):
        self.start = start
        self.finish = finish
        self.offset = offset
        self.points = []
        for i in points:
            self.points.append(i)

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
        self.frames_count = kw['frames_count']
        self.img_per_row_or_col = kw['img_per_row_or_col']
        self.color_key = kw['color_key']


class AnimationData:
    def __init__(self,kw):
        self.animationdata={}
        for key in kw:
            self.animationdata[key]=AnimationSingle(key,kw[key])


class MobSprite(pygame.sprite.Sprite):
    def __init__(self,data :AnimationData,fps:int,  x: int,y:int,path = None,move_speed=0,init_animation="IDLE",init_anim_speed=0,path_offset=[0,0],init_hp:int = None):
        pygame.sprite.Sprite.__init__(self)
        self.init_hp=init_hp
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



def cropp_img(path,frame_window_width,frame_window_height,border,start_x,start_y,frames_count,img_per_row_or_col,animation_orientation,color_key):
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
        pieces.append(pygame.Surface.subsurface(img,frame_x,frame_y,frame_window_width-border,frame_window_height-border))
        frame_index+=1
    return pieces

def load_level(road_name:str,road_tiles,database):
    road = read_images("img/road/", road_tiles, database["double_tile_size_xy"], (43, 45, 48))
    map = []
    map_size_tiles_xy = (40, 28)
    for i in range(map_size_tiles_xy[1]):
        map.append([""] * map_size_tiles_xy[0])
    building_map = {}


    road_map = pygame.image.load("img/Paths/"+road_name)
    road3x3_dictionary = read_road3x3_dictionary("img/Paths/")
    road3x3_dictionary_pixels = read_road3x3_dictionary_pixels("img/Paths/")
    road_map_mapping = read_road_map_mapping("img/Paths/mapping.csv")
    generate_map(map, road_map, road3x3_dictionary_pixels, road_map_mapping, map_size_tiles_xy)
    return map,road

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
            ret[x,y]=surf.get_at((x,y))
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


def generate_wave(number_of_mobs:int,mob_type,timestart:int,timeend:int,alghoritm="uniform"):
    wave=[]
    for i in range(number_of_mobs):
        wave.append((floor(uniform(timestart,timeend)),mob_type))
    return wave

def sort_sprites(e):
    return e.y
