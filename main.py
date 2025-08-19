from math import floor
from random import randint
import pygame
from pygame import K_LEFT, K_RIGHT, K_DOWN, K_UP, K_ESCAPE
from sys import exit
#from menus_utils import *
from create_menus import *
import time
from lvl_utils import *
from data import *

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
#tile_size_xy = (16, 16)
resolution_in_tiles=(100,56)

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
    "triple_tile_size_xy": (tile_size_xy[0]*3, tile_size_xy[1]*3),
    "quadrupal_tile_size_xy": (tile_size_xy[0]*4, tile_size_xy[1]*4),
    "half_tile_size_xy":(floor(tile_size_xy[0]/2), floor(tile_size_xy[1]/2)),
    #"resolution_in_tiles": (floor(resolution_xy[0] / tile_size_xy[0]), floor(resolution_xy[1] / tile_size_xy[1])),
    "resolution_in_tiles":resolution_in_tiles,
    "resolution_in_tiles_percent_xy":resolution_in_tiles_percent_xy,
    "lives": 10,
    "gold": 2000,
    "wave_number": 0,
    "font_sizes":fnt_sizes,
    "wave_menu_width_pt": 20,
    "building_allowed_map":{}
}


print(database)
screen = pygame.display.set_mode(database["resolution_xy"], pygame.FULLSCREEN)
#screen = pygame.display.set_mode(database["resolution_xy"])

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
turret_database=None
#archer_sprite=AnimationData(archer_sprite)
#catapult_sprite=AnimationData(catapult_sprite)

turret_sprites={}
turret_sprites["catapult_sprite"]=AnimationData(catapult_sprite)
turret_sprites["archer_sprite"]=AnimationData(archer_sprite)

projectiles=pygame.sprite.Group()
arrow_sprite=AnimationData(arrow_sprite)

is_game_on=False
while True:

    screen.fill("yellow")

    ### TURRETS
    turret_group.update(mobs,database,turret_database)
    turret_group.draw(screen)

    ### PROJECTILES
    projectiles.update()
    projectiles.draw(screen)
    for projectile in projectiles.sprites():
        if projectile.remove_me: projectiles.remove(projectile)

    ### MAP / VICTORY / STATS
    if is_game_on:
        print_road(screen, map, road,database["double_tile_size_xy"])

        wave_menu['WaveMenu/Stats/Lives'].update(txt="Lives: "+str(database["lives"]))

        wave_menu['WaveMenu/Info/Debug1'].update(txt=str(len(wave_mob)))
        if database['lives']<1:
            pass
            #after_wave(victory=False)

        if len(mobs_wave_units) ==0 and len(wave_mob)==0 and len(mobs)==0:
            is_game_on=False
            All_menus_groups_ordered = []
            #after_wave(victory=True)

    ### MOBS UPDATE N DRAW
    if mobs is not []:
        mobs.update()
        mobs_sprite_list = mobs.sprites()
        mobs_sprite_list.sort(key=sort_sprites)
        for mob in mobs_sprite_list:
            screen.blit(mob.image, mob.rect)

    ## SPAWN MOBS
    mobs,wave_mob=spawn_mobs(wave_mob,mobs,database,mob_path1_data)

    ### TERMINATE MOBS
    for mob in mobs:
        if mob.reached_finish:
            mobs.remove(mob)
            database['lives']-=1


    ### MENUS
    if All_menus_groups_ordered != []:
        for group in All_menus_groups_ordered:
            group[0].update(allowed_map=database["building_allowed_map"])

        groups, MMs = zip(*All_menus_groups_ordered)
        MMs=list(MMs)
        detect_menu_mouse_hoover(MMs)

        for group in groups:
            for mm in group.sprites(): mm.draw(screen)

    ### EVENTS
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
                All_menus_groups_ordered.append(create_world_menu(database))

            if events.dict["action"]=="start_battle":
                All_menus_groups_ordered = []
                is_game_on=True
                if "Title1" in events.dict["button_name"]:
                    map, road, building_allowed_map= load_level(levels_dict["umap"]["filename"], road_tiles, database)
                else:
                    map, road,building_allowed_map = load_level(levels_dict["zigzag"]["filename"], road_tiles, database)


                database["building_allowed_map"]=building_allowed_map
                tmp=create_wave_menu(database)
                All_menus_groups_ordered.append(tmp)
                wave_menu=tmp[1]
                mobs_wave_units = [30, 6, 10, 15, 20]
                wave_mob = generate_wave(mobs_wave_units.pop(0), AnimationData(goblin_sprite), pygame.time.get_ticks(),
                                         pygame.time.get_ticks() + (10 * 1000))
                wave_menu['WaveMenu/Stats/Gold'].update(txt="Gold: " + str(database["gold"]))
                wave_menu['WaveMenu/Stats/Wave'].update(txt="Wave: " + str(database["wave_number"]))

            if events.dict["action"]=="next_wave":
                if len(mobs_wave_units) > 0:
                    wave_mob+=generate_wave(mobs_wave_units.pop(0), AnimationData(goblin_sprite),
                                         pygame.time.get_ticks(),
                                         pygame.time.get_ticks() + (10 * 1000))
                    database["wave_number"]+=1
                    wave_menu['WaveMenu/Stats/Wave'].update(txt="Wave: " + str(database["wave_number"]))


            if events.dict["action"]=="build_turret":
                if database["gold"]>=events.dict["turret"].item.data["cost"]:
                    database["gold"]-=events.dict["turret"].item.data["cost"]
                    wave_menu['WaveMenu/Stats/Gold'].update(txt="Gold: " + str(database["gold"]))
                    turret_group.add(TurretSprite(turret_sprites[events.dict["turret"].item.data["sprite"]], pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], database["fps"], 100,10, (200,200), 5))
                    for turret in turret_group.sprites():
                        building_allowed_map = exclude_from_build_map(building_allowed_map, turret.rect)

            if events.dict["action"]=="shoot_projectile":
                if len(mobs) > 0:
                    target = get_target((events.dict["start_xy"][0], events.dict["start_xy"][1]),
                                        events.dict["turret_range"], events.dict["target_type"], mobs)
                    # projectiles.add(ProjectileSprite(arrow_sprite, fps, events.dict["start_xy"][0], events.dict["start_xy"][1],events.dict["projectile_speed"],target_xy=target))
                    if target is not None: projectiles.add(
                        ProjectileSprite(arrow_sprite, database["fps"], events.dict["start_xy"][0], events.dict["start_xy"][1],
                                         events.dict["projectile_speed"], events.dict["dmg"], target_sprite=target))



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
