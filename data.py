


projectile_init_database={
    "arrow":{
        "dmg_type":"single",
        "target_type":"mob",
        "sprite":"arrow_sprite",
        "projectile_speed":10
    },
    "bomb": {
        "dmg_type": "splash",
        "target_type":"ground",
        "sprite":"bomb_sprite",
        "scale":"quadrupal_tile_size_xy",
        "projectile_speed":5
    },
"rock": {
        "dmg_type": "single",
        "target_type":"mob",
        "sprite":"bomb_sprite",
        "scale":"quadrupal_tile_size_xy",
        "projectile_speed":5
    }


}

turret_init_database={
    "archer":
                  {"dmg":15,
                 "dmg_upgrade":2,
                 "dmg_change": "",
                 "atsp": 2000,
                 "atsp_upgrade":-50,
                 "atsp_change":"",
                 "range": 300,
                 "range_upgrade":10,
                 "range_change":"",
                 "food_price":10,
                 "buy_price":50,
                 "sell_price":50,
                 "upgrade_price":100,
                 "target_type":"most_hp",
                 "projectile_type":"arrow",
"projectile_speed":10,
                 "sprite_name":"archer_sprite"
        },
    "catapult":
        {"dmg": 50,
         "dmg_upgrade": 10,
         "dmg_change": "",
         "atsp": 4000,
         "atsp_upgrade": -200,
         "atsp_change": "",
         "range": 150,
         "range_upgrade": 10,
         "range_change": "",
         "food_price":30,
         "buy_price": 150,
         "sell_price": 75,
         "upgrade_price": 100,
         "target_type": "most_hp",
         "projectile_type":"bomb",
    "projectile_speed":5,
         "sprite_name": "catapult_sprite"
         },
    "cyclop":
        {"dmg": 25,
         "dmg_upgrade": 10,
         "dmg_change": "",
         "atsp": 1500,
         "atsp_upgrade": -200,
         "atsp_change": "",
         "range": 200,
         "range_upgrade": 10,
         "range_change": "",
         "buy_price": 150,
         "food_price":20,
         "sell_price": 75,
         "upgrade_price": 100,
         "target_type": "most_hp",
         "projectile_type": "rock",
         "projectile_speed": 5,
         "sprite_name": "cyclop_sprite"
         },

                 }


levels_dict={
 "umap":{
  "filename": "road_map1_40x28.png"
 },
 "umapc": {
  "filename": "road_mapc_40x28.png"
 },
 "zigzag":{
  "filename": "road_map2_40x28.png"
 },
 "zigzagc": {
  "filename": "road_map2c_40x28.png"
 },
 "bulb": {
  "filename": "road_mapBULBc_40x28.png"
 },
 "cos": {
  "filename": "road_mapCOSc_40x28.png"
 },
 "long": {
  "filename": "road_mapLONGc_40x28.png"
 },
 "zmap": {
  "filename": "road_mapZc_40x28.png"
 }

}


map1=[
 ["","wsd","wsad","wsa","","","","","","","","","","","wsd","wsad","wsa",""],
 ["","wsd","wsad","wsa","","","","","","","","","","","wsd","wsad","wsa",""],
 ["","wsd","wsad","wsa","","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["", "wsd","wsad", "wsa",  "","","","","","","","","","","wsd","wsad","wsa",""],
 ["","wsd","wsad","Xwd","sad","sad","sad","sad","sad","sad","sad","sad","sad","sad","Xwa","wsad","wsa","",""],
 ["","wsd","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsad","wsa",""],
 ["","wd","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wad","wa","",""],
]
road_tiles = {
"sd":"road_1.png",
"sad":"road_2.png",
"sa":"road_3.png",
"wsd":"road_4.png",
"wsad":"road_5.png",
"wsa":"road_6.png",
"wd":"road_7.png",
"wad":"road_8.png",
"wa":"road_9.png",
"Xsd":"road_10.png",
"Xsa":"road_11.png",
"Xwd":"road_12.png",
"Xwa":"road_13.png"
}
road_tiles_old = {
"sd":"img/road/road_1.png",
"sad":"img/road/road_2.png",
"sa":"img/road/road_3.png",
"wsd":"img/road/road_4.png",
"wsad":"img/road/road_5.png",
"wsa":"img/road/road_6.png",
"wd":"img/road/road_7.png",
"wad":"img/road/road_8.png",
"wa":"img/road/road_9.png",
"Xsd":"img/road/road_10.png",
"Xsa":"img/road/road_11.png",
"Xwd":"img/road/road_12.png",
"Xwa":"img/road/road_13.png"
}

mob_path1_data={
 'START' : [64,20],
 'POINTS': [[64,476],[476,476],[476,0]],
 'FINISH' : [476,0]
}
mob_path2_data={
 'START': [20, 20],
 'POINTS': [[20, 320], [400, 320], [400, 120],[300,120],[300,220],[500,220],[500,20]],
 'FINISH': [500, 20]
}
animation_sprites={}
animation_sprites["bomb_sprite"] = {
'IDLE': {
'path': "img/bomg.png",
'frame_window_width':32,
'frame_window_height':16,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':6,
'init_rotation':90,
'start_x':0,
'start_y':0,
'frames_count':5,
'img_per_row_or_col':5,
'color_key':(0,0,0)
},
'HIT': {
'path': "img/bomb_explode.png",
'frame_window_width':16,
'frame_window_height':16,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(0,0,0)
}
}
animation_sprites["arrow_sprite"] = {
'IDLE': {
'path': "img/arrow3.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':1,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}
}
animation_sprites["spider_sprite"] = {

'IDLE': {
'path': "img/mobs/spider/spider_down.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':4,
'color_key':(255,255,255)
},
'WALK_DOWN': {
'path': "img/mobs/spider/spider_down.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(255,255,255)
},
'WALK_UP': {
'path': "img/mobs/spider/spider_up.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(255,255,255)
},
'WALK_LEFT': {
'path': "img/mobs/spider/spider_left.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(255,255,255)
},
'WALK_RIGHT': {
'path': "img/mobs/spider/spider_right.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(255,255,255)
}}

### GOBLIN
animation_sprites["goblin_sprite"] = {
'WALK_DOWN': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
},
'IDLE': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
},
'WALK_LEFT': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':64,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
 },
'WALK_RIGHT': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':128,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
},
'WALK_UP': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':0,
'start_y':192,
'frames_count':3,
'img_per_row_or_col':3,
'color_key':(255,255,255)
}
}
### /GOBLIN
### SKELETON
animation_sprites["skeleton_sprite"] = {
'IDLE': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
'WALK_DOWN': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':0,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
'WALK_LEFT': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':64,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
'WALK_RIGHT': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':128,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
'WALK_UP': {
'path': "img/zombie_n_skeleton2.png",
'frame_window_width':32,
'frame_window_height':64,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':10,
'start_x':96,
'start_y':192,
'frames_count':6,
'img_per_row_or_col':6,
'color_key':(255,255,255)
},
}

### /SKELETON

animation_sprites["catapult_sprite"]={
 'FIRE':{
'path': "img/Turrets/catapult/catapult.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'fire_at_frame':4,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':7,
'img_per_row_or_col':7,
'color_key':(0,0,0)
},
'IDLE': {
'path': "img/Turrets/catapult/catapult.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':5,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}
}

animation_sprites["cyclop_sprite"]={
 'FIRE':{
'path': "img/Turrets/cyclop/cyclop.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'fire_at_frame':6,
'anim_fps':10,
'start_x':0,
'start_y':0,
'frames_count':7,
'img_per_row_or_col':7,
'color_key':(0,0,0)
},
'IDLE': {
'path': "img/Turrets/cyclop/cyclop.png",
'frame_window_width':32,
'frame_window_height':32,
'animation_orientation':"horizontal",
'border':0,
'anim_fps':5,
'start_x':0,
'start_y':0,
'frames_count':1,
'img_per_row_or_col':1,
'color_key':(0,0,0)
}
}
### ARCHER
animation_sprites["archer_sprite"]={
'WALK_RIGHT': {
'path': "img/anim.png",
'frame_window_width':73,
'frame_window_height':73,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':10,
'start_x':129,
'start_y':185,
'frames_count':10,
'img_per_row_or_col':5,
'color_key':(79,143,186)
},
'FIRE': {
'path': "img/anim.png",
'frame_window_width':73,
'frame_window_height':73,
'animation_orientation':"horizontal",
'border':1,
'fire_at_frame':10,
'anim_fps':20,
'start_x':129,
'start_y':406,
'frames_count':17,
'img_per_row_or_col':5,
'color_key':(79,143,186)
},
'IDLE': {
'path': "img/anim.png",
'frame_window_width':73,
'frame_window_height':73,
'animation_orientation':"horizontal",
'border':1,
'anim_fps':5,
'start_x':129,
'start_y':111,
'frames_count':4,
'img_per_row_or_col':4,
'color_key':(79,143,186)
}
}
