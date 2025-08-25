from lvl_utils import *

levels_list={}


wave1=MobWave()
wave1.add(BunchOfMobs(6,"goblin_sprite"))
wave2=MobWave()
wave2.add(BunchOfMobs(12,"goblin_sprite"))
wave3=MobWave()
wave3.add(BunchOfMobs(24,"goblin_sprite"))
wave4=MobWave()
wave4.add(BunchOfMobs(48,"goblin_sprite"))


levels_list[1]=Level("umapc")
levels_list[1].add_wave(wave1)
levels_list[1].add_wave(wave2)

levels_list[2]=Level("zigzagc")
levels_list[2].add_wave(wave1)
levels_list[2].add_wave(wave2)
levels_list[2].add_wave(wave3)

levels_list[3]=Level("zigzagc")
levels_list[3].add_wave(wave1)
levels_list[3].add_wave(wave2)
levels_list[3].add_wave(wave3)


levels_list[4]=Level("zigzagc")
levels_list[4].add_wave(wave1)
levels_list[4].add_wave(wave2)
levels_list[4].add_wave(wave3)
levels_list[4].add_wave(wave4)

levels_list[5]=Level("zigzagc")
levels_list[5].add_wave(wave1)
levels_list[5].add_wave(wave2)
levels_list[5].add_wave(wave3)
levels_list[5].add_wave(wave4)

levels_list[6]=Level("zigzagc")
levels_list[6].add_wave(wave1)
levels_list[6].add_wave(wave2)
levels_list[6].add_wave(wave3)
levels_list[6].add_wave(wave4)

print(levels_list[1].waves[0].bunches[0].mob)