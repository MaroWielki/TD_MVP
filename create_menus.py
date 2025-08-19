import pygame
from math import floor

from menus_utils import *
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
    LM = {}
    level_menu = pygame.sprite.Group()

    level_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                            (database["resolution_in_tiles_percent_xy"][0][0],
                             database["resolution_in_tiles_percent_xy"][0][1]),
                            (database["resolution_in_tiles_percent_xy"][110][0],
                             database["resolution_in_tiles_percent_xy"][110][1]), "LevelMenu", "",
                            tile_size_xy=database["tile_size_xy"], draggable=False))
    LM['LevelMenu'] = get_member_by_name(level_menu.sprites(), "LevelMenu")

    lvl_menu_grid=([10],[20])
    coords_x=0
    coords_y=0

    ### CENTER
    #LM['LevelMenu/Title0'] = LM['LevelMenu'].add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,(database["resolution_in_tiles_percent_xy"][lvl_menu_grid[0][coords_x]][0],database["resolution_in_tiles_percent_xy"][lvl_menu_grid[1][coords_y]][1]),(database["resolution_in_tiles_percent_xy"][30][0],database["resolution_in_tiles_percent_xy"][15][1]), "LevelMenu/Title0", "Title0",tile_size_xy=database["double_tile_size_xy"], draggable=True))
    LM['LevelMenu/Title0'] = LM['LevelMenu'].add(MenuTitle(LM['LevelMenu'].px_start_xy, database, (
        database["resolution_in_tiles_percent_xy"][lvl_menu_grid[0][coords_x]][0],
        database["resolution_in_tiles_percent_xy"][lvl_menu_grid[1][coords_y]][1]),
                                                           (database["resolution_in_tiles_percent_xy"][30][0],
                                                            database["resolution_in_tiles_percent_xy"][15][1]),
                                                           "LevelMenu/Title0", "Title0",
                                                           tile_size_xy=database["double_tile_size_xy"],
                                                           draggable=True))

    LM['LevelMenu/Title0/Text0']=LM['LevelMenu/Title0'].add(MenuText(LM['LevelMenu/Title0'].px_start_xy, database, (1, 7), "LevelMenu/Title0/Text0","init txt"))

    LM['LevelMenu/Title0/button0'] = LM['LevelMenu/Title0'].add(
        MenuButton(LM['LevelMenu/Title0'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][45][0], 3),
                   (database["resolution_in_tiles_percent_xy"][10][0] * 4, 8), "LevelMenu/Title0/button0",
                   text="Shop", color=3, action="open_shop"))

    LM['LevelMenu/Title0/button1'] = LM['LevelMenu/Title0'].add(
        MenuButton(LM['LevelMenu/Title0'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][45][0], 6),
                   (database["resolution_in_tiles_percent_xy"][10][0] * 4, 8), "LevelMenu/Title0/button1",
                   text="Armory", color=3, action="open_armory"))

    ### ACTIVE
    LM['LevelMenu/Title0/Title0'] = LM['LevelMenu/Title0'].add(
        MenuTitle(LM['LevelMenu/Title0'].px_start_xy, database,
                  (5,1),
                  (5,3), "LevelMenu/Title0/Title0", "Active",
                  tile_size_xy=database["double_tile_size_xy"], draggable=False))

    LM['LevelMenu/Title0/Title0/grid0'] = LM['LevelMenu/Title0/Title0'].add(GuiGrid(LM['LevelMenu/Title0/Title0'].px_start_xy, database, (0.5, 1.25),(4,1), "LevelMenu/Title0/Title0/grid0",tile_size_xy=database["double_tile_size_xy"]))

    ### INACTIVE
    LM['LevelMenu/Title0/Title1'] = LM['LevelMenu/Title0'].add(
        MenuTitle(LM['LevelMenu/Title0'].px_start_xy, database,
                  (11, 1),
                  (5, 6), "LevelMenu/Title0/Title1", "InActive",
                  tile_size_xy=database["double_tile_size_xy"], draggable=False))
    LM['LevelMenu/Title0/Title1/grid0'] = LM['LevelMenu/Title0/Title1'].add(GuiGrid(LM['LevelMenu/Title0/Title0'].px_start_xy, database, (0.5, 1.25),(4,4), "LevelMenu/Title0/Title1/grid0",tile_size_xy=database["double_tile_size_xy"]))

    inactive_item_index=0

    LM['LevelMenu/Title0/Title1/grid0/item'+str(inactive_item_index)] = LM['LevelMenu/Title0/Title1/grid0'].add(
        ItemMenu(LM['LevelMenu/Title0/Title1/grid0'].px_start_xy, database, (2, 0),  "LevelMenu/Title0/Title1/grid0/item"+str(inactive_item_index),tile_size_xy=database["double_tile_size_xy"],item_name="catapult",parent_grid=LM['LevelMenu/Title0/Title1/grid0']))


    ### WORLDS
    #lvl_menu_grid=([10,40,70],[10,75])
    lvl_menu_grid=([5,20,35],[5,37])  # Halved becouse double sized

    lvl_menu_size_xy=(12,15)

    index=1
    for coords_x in range(3):
        for coords_y in range(2):
            LM['LevelMenu/Title'+str(index)] = LM['LevelMenu'].add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                            (database["resolution_in_tiles_percent_xy"][lvl_menu_grid[0][coords_x]][0],
                             database["resolution_in_tiles_percent_xy"][lvl_menu_grid[1][coords_y]][1]),
                            (database["resolution_in_tiles_percent_xy"][lvl_menu_size_xy[0]][0],
                             database["resolution_in_tiles_percent_xy"][lvl_menu_size_xy[1]][1]), "Title"+str(index), "Title"+str(index),
                            tile_size_xy=database["double_tile_size_xy"], draggable=False))

            LM['LevelMenu/Title'+str(index)+'/button0'] = LM['LevelMenu/Title'+str(index)].add(
                MenuButton(LM['LevelMenu/Title'+str(index)].px_start_xy, database,
                           (database["resolution_in_tiles_percent_xy"][7][0], database["resolution_in_tiles_percent_xy"][(lvl_menu_size_xy[1]*2)-6][1]),
                           (database["resolution_in_tiles_percent_xy"][10][0] * 4, 8), 'LevelMenu/Title'+str(index)+'/button0',
                           text="To battle!", color=3, action="start_battle"))
            index+=1


    return level_menu,LM


def create_wave_menu(database):
    LM = {}
    level_menu = pygame.sprite.Group()

    level_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                             (database["resolution_in_tiles_percent_xy"][80][0],
                              database["resolution_in_tiles_percent_xy"][0][1]),
                             (database["resolution_in_tiles_percent_xy"][20][0],
                              database["resolution_in_tiles_percent_xy"][100][1]), "WaveMenu", "",
                             tile_size_xy=database["tile_size_xy"], draggable=False))
    LM['WaveMenu'] = get_member_by_name(level_menu.sprites(), "WaveMenu")

    LM['WaveMenu/Stats']=LM['WaveMenu'].add(MenuTitle(LM['WaveMenu'].px_start_xy, database,
                             (0,0),
                             (database["resolution_in_tiles_percent_xy"][10][0],
                              database["resolution_in_tiles_percent_xy"][10][1]), "WaveMenu/Stats", "Stats",
                             tile_size_xy=database["double_tile_size_xy"], draggable=False))

    LM['WaveMenu/Stats/Lives'] = LM['WaveMenu/Stats'].add(
        MenuText(LM['WaveMenu/Stats'].px_start_xy, database, (1, 2), "WaveMenu/Stats/Lives", "Lives: "))

    LM['WaveMenu/Stats/NextWave']= LM['WaveMenu/Stats'].add(MenuButton(LM['WaveMenu/Stats'].px_start_xy, database, (database["resolution_in_tiles_percent_xy"][10][0], 2),
                   (database["resolution_in_tiles_percent_xy"][7][0] * 4, 8), "WaveMenu/Stats/NextWave",
                   text="Next Wave", color=3, action="next_wave"))


    LM['WaveMenu/Details']=LM['WaveMenu'].add(MenuTitle(LM['WaveMenu'].px_start_xy, database,
                             (0,
                              database["resolution_in_tiles_percent_xy"][10][1]),
                             (database["resolution_in_tiles_percent_xy"][10][0],
                              database["resolution_in_tiles_percent_xy"][20][1]), "WaveMenu/Details", "Details",
                             tile_size_xy=database["double_tile_size_xy"], draggable=False))

    LM['WaveMenu/Shop']=LM['WaveMenu'].add(MenuTitle(LM['WaveMenu'].px_start_xy, database,
                             (0,
                              database["resolution_in_tiles_percent_xy"][30][1]),
                             (database["resolution_in_tiles_percent_xy"][10][0],
                              database["resolution_in_tiles_percent_xy"][17][1]), "WaveMenu/Shop", "Shop",
                             tile_size_xy=database["double_tile_size_xy"], draggable=False))

    LM['WaveMenu/Info']=LM['WaveMenu'].add(MenuTitle(LM['WaveMenu'].px_start_xy, database,
                             (0,
                              database["resolution_in_tiles_percent_xy"][45][1]),
                             (database["resolution_in_tiles_percent_xy"][10][0],
                              database["resolution_in_tiles_percent_xy"][10][1]), "WaveMenu/Info", "Info",
                             tile_size_xy=database["double_tile_size_xy"], draggable=False))
    LM['WaveMenu/Info/Debug0'] = LM['WaveMenu/Info'].add(
        MenuText(LM['WaveMenu/Info'].px_start_xy, database, (1, 2), "WaveMenu/Info/Debug0", "debug0: "))
    LM['WaveMenu/Info/Debug1'] = LM['WaveMenu/Info'].add(
        MenuText(LM['WaveMenu/Info'].px_start_xy, database, (1, 3), "WaveMenu/Info/Debug1", "Debug1: "))

    return level_menu, LM