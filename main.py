


from sys import exit

import pygame.sprite
from pygame import K_ESCAPE
import menus_utils
#from menus_utils import *
from create_menus import *


from lvl_utils import *
from data import *
#from mob_waves import *

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


            if selected_turret is not None and (colliding_objects == [] or menus_utils.MenuTitle not in [type(a) for a in colliding_objects]):

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

    real_fps=pygame.time.get_ticks() - last_update_time
    last_update_time = pygame.time.get_ticks()
    pygame.display.set_caption(str(floor(1000/real_fps)))
