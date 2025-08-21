



import pygame
pygame.init()




screen=pygame.display.set_mode((800,600))

folder = "img/GUI/1 Interface/"

im = pygame.image.load(folder + "Tile_93.png").convert()
print(im)
im2 = pygame.transform.smoothscale(im, (13, 13))
#'GENERIC', 'MMX', 'SSE'

im3 = pygame.transform.scale(im, (32, 32))
pygame.transform.set_smoothscale_backend('GENERIC')

img4=pygame.transform.smoothscale(im, (26, 26))

p1=im.subsurface((0,0,7,6))
p2=im.subsurface((10,0,6,7))
p3=im.subsurface((0,10,7,6))
p4=im.subsurface((10,10,6,7))

while True:
    screen.fill("green")

    screen.blit(im, (100, 100))
    screen.blit(im2, (150, 100))
    screen.blit(im3, (200, 100))
    screen.blit(img4, (250, 100))

    screen.blit(p1, (250, 100))
    screen.blit(p2, (300, 100))
    screen.blit(p3, (350, 100))
    screen.blit(p4, (400, 100))

    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()



