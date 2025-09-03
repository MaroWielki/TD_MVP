from random import randint

import pygame
from gui_tiles import *
from math import floor

from lvl_utils import TurretSprite
from mob_waves import *

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



