import pygame

available_turrets=["archer","catapult","cyclop"]
available_enemies=["goblin","spider","skeleton","human","snake","soldier",]
available_bosses=["eye"]
available_bosses_price=["victory"]
available_prices=["chicken","steak","gem","random_turret"]
#available_prices=["chicken","steak","gem","random_turret","random_item"]

prices_chances={
1:
                    {
                        "chicken":80,
                        "steak":10,
                        "gem":5,
                        "random_turret":5
                    },
2:
                    {
                        "chicken":70,
                        "steak":20,
                        "gem":5,
                        "random_turret":5
                    },
3:
                    {
                        "chicken":60,
                        "steak":30,
                        "gem":5,
                        "random_turret":5
                    },
4:
                    {
                        "chicken":50,
                        "steak":10,
                        "gem":10,
                        "random_turret":10
                    },
5:
                    {
                        "chicken":10,
                        "steak":50,
                        "gem":20,
                        "random_turret":20
                    },
6:
    {
                "victory":100, }
}

enemies_chances={
1:
                    {
                        "spider":60,
                        "skeleton":70,
                        "human":5,
                        "wolf":0,
                        "snake":0,
                        "goblin":0,
                        "soldier":0,
                        "eye":0
                    },
2:
                    {
                        "spider":60,
                        "skeleton":40,
                        "human":30,
                        "wolf":10,
                        "snake":0,
                        "goblin":0,
                        "soldier":0,
                        "eye":0
                    },
3:
                    {
                        "spider":60,
                        "skeleton":20,
                        "human":40,
                        "wolf":20,
                        "snake":40,
                        "goblin":0,
                        "soldier":0,
                        "eye":0
                    },
4:
                    {
                        "spider":30,
                        "skeleton":0,
                        "human":0,
                        "wolf":60,
                        "snake":20,
                        "goblin":60,
                        "soldier":10,
                        "eye":0
                    },
5:
                    {
                        "spider":80,
                        "skeleton":0,
                        "human":0,
                        "wolf":40,
                        "snake":20,
                        "goblin":30,
                        "soldier":70,
                        "eye":0
                    },
6:
    {
        "spider": 0,
        "skeleton": 0,
        "human": 0,
        "wolf": 100,
        "snake": 0,
        "goblin": 100,
        "soldier": 100,
        "eye": 100
    }
}

mob_database={
    "goblin_sprite":{
        "init_hp":125,
        "speed":1,
        "award": 15
    },
    "human_sprite":{
        "init_hp": 85,
        "speed": 2,
        "award": 10

    },
    "snake_sprite": {
        "init_hp": 85,
        "speed": 1.75,
        "award": 15

    },
    "soldier_sprite": {
        "init_hp": 200,
        "speed": 1.25,
        "award": 20

    },
    "wolf_sprite": {
        "init_hp": 45,
        "speed": 3,
        "award": 10

    },
    "skeleton_sprite":{
        "init_hp":50,
        "speed":2,
        "award": 10
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
        "sprite": "random_turret_sprite",
    "description":"random turret",
        "description1": "",
"description2": "",
"description3": ""
    },
    "victory": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "victory_sprite",
        "description":"game victory",
        "description1": "",
"description2": "",
"description3": ""
    },
    "random_item": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "random_item_sprite",
        "description":" random item",
        "description1": "",
"description2": "",
"description3": ""
    },
    "eye": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "eye_sprite",
        "description":"Eye of despair",
        "description1": "",
"description2": "",
"description3": ""
    },
    "human":{
        "size": (1, 1),
        "scale": 1,
        "sprite": "human_sprite",
        "description":"Lost Human",
        "description1": "",
"description2": "",
"description3": ""
    },
    "soldier":{
        "size": (1, 1),
        "scale": 1,
        "sprite": "soldier_sprite",
        "description":"Heavy knight",
        "description1": "",
"description2": "",
"description3": ""
    },
    "snake":{
        "size": (1, 1),
        "scale": 1,
        "sprite": "snake_sprite",
        "description":"Ninja",
        "description1": "",
"description2": "",
"description3": ""
    },
    "wolf":{
        "size": (1, 1),
        "scale": 1,
        "sprite": "wolf_sprite",
        "description":"Warewolf",
        "description1": "",
"description2": "",
"description3": ""
    },
    "shirt":{
        "size":(2,2),
        "scale":2
    },
    "gem":{
        "size":(1,1),
        "scale": 1,
        "sprite": "gem_sprite",
        "description":"+ 1 gem",
        "description1": "",
"description2": "",
"description3": ""
    },
    "chicken": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "chicken_sprite",
        "description":"+1 food",
        "description1": "",
"description2": "",
"description3": ""
    },
    "steak": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "steak_sprite",
        "description":"+3 food",
        "description1": "",
"description2": "",
"description3": ""
    },
    "goblin": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "goblin_sprite",
        "description":"fearsome goblin",
        "description1": "",
"description2": "",
"description3": ""
    },
    "spider": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "spider_sprite",
        "description":"spider sprinter",
        "description1": "",
"description2": "",
"description3": ""
    },
    "skeleton": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "skeleton_sprite"
,
        "description":"good old skeleton",
        "description1": "",
"description2": "",
"description3": ""
    },


    "catapult":{
        "size":(1,1),
        "scale":1,
        "sprite":"catapult_sprite",
        "cost": 100,
        "food_cost":3,
"gems_cost":0,
        "name":"catapult",
        "description":"catapult",
        "description1":"cost: 3 food",
"description2": "",
"description3": ""
    },
    "archer": {
        "size": (1, 1),
        "scale": 1,
        "sprite":"archer1_sprite",
        "cost": 50,
"food_cost":2,
"gems_cost":0,
        "name":"archer",
        "description": "archer",
        "description1": "cost: 2 food",
"description2": "",
"description3": ""
    },
    "cyclop": {
        "size": (1, 1),
        "scale": 1,
        "sprite": "cyclop_sprite",
        "cost": 100,
"food_cost":2,
        "gems_cost":0,
        "name": "cyclop",
        "description": "cyclop",
        "description1": "cost: 2 food",
"description2": "",
"description3": ""
    }
}



class Item:
    def __init__(self, tile_size_xy:tuple,name):
        self.name=name
        self.data=item_data[name]
        img=pygame.image.load("img/items/"+name+".png")
        img.set_colorkey((255,255,255))
        self.image=pygame.transform.scale(img,(tile_size_xy[0]*self.data["scale"],tile_size_xy[1]*self.data["scale"]))



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