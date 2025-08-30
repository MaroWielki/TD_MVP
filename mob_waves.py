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

    for index in range(0,6):

        for mob in input[index]:
            wave = MobWave()
            wave.add(BunchOfMobs(12,item_data[mob]["sprite"]))
            levels_list[index+1].add_wave(wave)
    return levels_list