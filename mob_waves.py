from gui_tiles import item_data
from lvl_utils import *

# levels_list={}
#
# wave0=MobWave()
# wave0.add(BunchOfMobs(6,"spider_sprite"))
# wave1=MobWave()
# wave1.add(BunchOfMobs(6,"goblin_sprite"))
# wave2=MobWave()
# wave2.add(BunchOfMobs(12,"goblin_sprite"))
# wave3=MobWave()
# wave3.add(BunchOfMobs(24,"goblin_sprite"))
# wave4=MobWave()
# wave4.add(BunchOfMobs(48,"goblin_sprite"))
# wave5=MobWave()
# wave5.add(BunchOfMobs(6,"skeleton_sprite"))
#
#
# levels_list[1]=Level("umapc")
# levels_list[1].add_wave(wave0)
# levels_list[1].add_wave(wave5)
#
# levels_list[2]=Level("zigzagc")
# levels_list[2].add_wave(wave1)
# levels_list[2].add_wave(wave2)
# levels_list[2].add_wave(wave3)
#
# levels_list[3]=Level("bulb")
# levels_list[3].add_wave(wave1)
# levels_list[3].add_wave(wave2)
# levels_list[3].add_wave(wave3)
#
#
# levels_list[4]=Level("cos")
# levels_list[4].add_wave(wave1)
# levels_list[4].add_wave(wave2)
# levels_list[4].add_wave(wave3)
# levels_list[4].add_wave(wave4)
#
# levels_list[5]=Level("zmap")
# levels_list[5].add_wave(wave1)
# levels_list[5].add_wave(wave2)
# levels_list[5].add_wave(wave3)
# levels_list[5].add_wave(wave4)
#
# levels_list[6]=Level("long")
# levels_list[6].add_wave(wave1)
# levels_list[6].add_wave(wave2)
# levels_list[6].add_wave(wave3)
# levels_list[6].add_wave(wave4)

def wave_generator(input):
    levels_list={}

    wave0 = MobWave()
    wave0.add(BunchOfMobs(6, "spider_sprite"))

    levels_list[1] = Level("umapc")
    levels_list[2] = Level("zigzagc")
    levels_list[3] = Level("bulb")
    levels_list[4] = Level("cos")
    levels_list[5] = Level("zmap")
    levels_list[6] = Level("long")

    mobs_in_bunch = {"spider": 10, "skeleton": 4, "goblin": 5, "eye": 4,"human":4,"snake": 6,"soldier":5,"wolf":6}
    waves_in_lvl = {1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8}
    bunches_in_wave = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 4,7:7,8:10}


    for lvl_index in range(1,7):
        for wave_index in range(waves_in_lvl[lvl_index]):
            wave=MobWave()
            for bunch_index in range(bunches_in_wave[wave_index+1]):
                mob=input[lvl_index-1][randint(0,len(input[lvl_index-1])-1)]
                wave.add(BunchOfMobs(mobs_in_bunch[mob],item_data[mob]["sprite"]))
            levels_list[lvl_index].add_wave(wave)


        # for mob in input[index]:
        #     wave = MobWave()
        #     wave.add(BunchOfMobs(12,item_data[mob]["sprite"]))
        #     levels_list[index+1].add_wave(wave)

    return levels_list