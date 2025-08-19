import time

map={}



t=time.time()
for x in range(1000):
    for y in range(1000):
        if x+y%2==1:
            map[x,y]=True
        else:
            map[x,y]=False
print(time.time()-t)

t=time.time()
map2=[[False for x in range(1000)] for y in range(1000)]

print(time.time()-t)

t=time.time()
for x in range(1000):
    for y in range(1000):
        if x+y%2==1:
            map2[x][y]=True
        else:
            map2[x][y]=False
print(time.time()-t)

print(map2[100][200])