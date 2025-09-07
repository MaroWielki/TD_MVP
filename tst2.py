a="ArmoryMenu/grid2ButtonDMG"
print(a[-3:])



import pygame
from random import randint
pygame.init()

screen=pygame.display.set_mode((800,600))

img=pygame.image.load("img/items/human.png")
img.set_colorkey((255,255,255))
print(img.get_at((0,0)))
img2=pygame.image.load("img/items/eye.png").convert()
img2.set_colorkey((0,0,0))
print(img2.get_at((0,0)))


while True:
    screen.fill("green")
    screen.blit(img,(0,0))
    screen.blit(img2,(200,0))
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()