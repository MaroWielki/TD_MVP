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