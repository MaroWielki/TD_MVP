from math import floor
from random import randint
import pygame
from pygame import K_LEFT, K_RIGHT, K_DOWN, K_UP, K_ESCAPE
from sys import exit
#from menus_utils import *
from create_menus import *
import time


pygame.init()
pygame.display.set_caption("Marek")
clock = pygame.time.Clock()
last_update_time = pygame.time.get_ticks()

#resolution_xy = (1600, 900)
#resolution_xy = (1400, 800)
resolution_xy = (1366,768)
#resolution_xy = (800, 600)
#resolution_xy = (1066, 600)
#tile_size_xy = (16, 16)
resolution_in_tiles=(100,56)
#fnt_sizes=tab=get_fonts_sizes(["arial"],[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])
fnt_list=["arial","comicsansms"]

fnt_sizes=tab=get_fonts_sizes(fnt_list,list(range(6,30)))


tile_size_xy= (floor(resolution_xy[0]/resolution_in_tiles[0]), floor(resolution_xy[1]/resolution_in_tiles[1]))
resolution_in_tiles_percent_xy = {}
for p in range(150):
    resolution_in_tiles_percent_xy[p] = (floor(resolution_in_tiles[0] * p / 100),
                                         floor(resolution_in_tiles[1] * p / 100))


database = {
    "fps": 60,
    "resolution_xy": resolution_xy,
    "tile_size_xy": tile_size_xy,
    "double_tile_size_xy": (tile_size_xy[0]*2, tile_size_xy[1]*2),
    "half_tile_size_xy":(floor(tile_size_xy[0]/2), floor(tile_size_xy[1]/2)),
    #"resolution_in_tiles": (floor(resolution_xy[0] / tile_size_xy[0]), floor(resolution_xy[1] / tile_size_xy[1])),
    "resolution_in_tiles":resolution_in_tiles,
    "resolution_in_tiles_percent_xy":resolution_in_tiles_percent_xy,
    "lives": 10,
    "gold": 50,
    "wave_number": 1,
    "font_sizes":fnt_sizes
}


print(database)
screen = pygame.display.set_mode(database["resolution_xy"], pygame.FULLSCREEN)
#screen = pygame.display.set_mode(database["resolution_xy"])



All_menus_groups_ordered=[]
#inv_menu,IM = create_inventory_menu(database)
#test_menu,TM=create_test_menu(database)

inv_menu_index=0
#All_menus_groups_ordered.append(create_inventory_menu(database))
#All_menus_groups_ordered.append(create_test_menu(database,inv_menu_index))
#All_menus_groups_ordered.append(create_chest_menu(database))
All_menus_groups_ordered.append(create_main_menu(database))



while True:

    screen.fill("yellow")

    if All_menus_groups_ordered != []:
        for group in All_menus_groups_ordered:
            group[0].update()

        groups, MMs = zip(*All_menus_groups_ordered)
        MMs=list(MMs)
        detect_menu_mouse_hoover(MMs)

        for group in groups:
            for mm in group.sprites(): mm.draw(screen)

    #for mm in inv_menu.sprites(): mm.draw(screen)
    #for mm in test_menu.sprites(): mm.draw(screen)


    for events in pygame.event.get():

        ###### MOUSE DOWN
        if events.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            colliding_objects=find_colliding_objects(mouse_pos,MMs)
            if events.button == 1:
                handle_LMB_down(colliding_objects,mouse_pos)
                bring_root_to_front(colliding_objects, All_menus_groups_ordered)
            if events.button == 3:
                handle_RMB_down(colliding_objects,mouse_pos)
                bring_root_to_front(colliding_objects, All_menus_groups_ordered)
        ###### MOUSE UP
        if events.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            colliding_objects = find_colliding_objects(mouse_pos, MMs)
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


            if events.dict["action"] == "create_test_menu":
                inv_menu_index+=1
                All_menus_groups_ordered.append(create_test_menu(database, inv_menu_index))

            if events.dict["action"]=="move_item_from_grid_to_grid":
                move_item_from_grid_to_grid(events.dict,All_menus_groups_ordered,database)

            if events.dict["action"]=="quit_game":
                pygame.quit()
                exit()

            if events.dict["action"]=="start_new_game":
                All_menus_groups_ordered= []
                All_menus_groups_ordered.append(create_lvl_menu(database))


        ##### QUIT
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
        if events.type == pygame.KEYDOWN:
            if events.key == K_ESCAPE:
                pygame.quit()
                exit()

    # s = pygame.Surface((1366, 768))
    # s.set_alpha(100)
    # s.fill("red")
    # screen.blit(s, (0, 0))
    #

    pygame.display.update()
    clock.tick(database["fps"])

    real_fps=pygame.time.get_ticks() - last_update_time
    last_update_time = pygame.time.get_ticks()
    pygame.display.set_caption(str(floor(1000/real_fps)))
