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



def create_lvl_menu(database):
    LM = {}
    level_menu = pygame.sprite.Group()

    level_menu.add(MenuTitle(get_xy((0, 0), database["tile_size_xy"], 0, 0), database,
                            (database["resolution_in_tiles_percent_xy"][0][0],
                             database["resolution_in_tiles_percent_xy"][0][1]),
                            (database["resolution_in_tiles_percent_xy"][100][0],
                             database["resolution_in_tiles_percent_xy"][100][1]), "LevelMenu", "",
                            tile_size_xy=database["tile_size_xy"], draggable=False))
    MM['LevelMenu'] = get_member_by_name(level_menu.sprites(), "LevelMenu")

    return level_menu,LM