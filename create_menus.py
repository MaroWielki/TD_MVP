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
                             database["resolution_in_tiles_percent_xy"][lvl_menu_size_xy[1]][1]), "Title"+str(index), "Title"+str(index),
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