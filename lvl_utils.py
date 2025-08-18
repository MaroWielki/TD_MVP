import pygame
from math import floor

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
    for x in range(16):
        for y in range(16):
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