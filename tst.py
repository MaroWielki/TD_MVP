



import pygame
pygame.init()


def sort_fun(a:list):
    return a[1]

img=pygame.image.load("img/Paths/road_mapc_40x28.png")
list=[]
print(img)
for x in range(img.get_width()):
    for y in range(img.get_height()):
        if img.get_at((x,y))[0] in range(1,254):
            list.append(((x,y),img.get_at((x,y))[0]))



print(list)
list.sort(key=sort_fun)
print(list)

dic={}
st=list.pop(0)
dic["START"]=[st[0][0],st[0][1]]
dic["POINTS"]=[]
for pt in list:
    dic["POINTS"].append([pt[0][0],pt[0][1]])
dic["FINISH"]=[list[-1][0][0],list[-1][0][1]]


print(dic)
pygame.quit()
exit()



