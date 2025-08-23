



import pygame
from random import randint
pygame.init()

screen=pygame.display.set_mode((800,600))

#im = pygame.image.load(folder + "Tile_93.png").convert()
kostka_wartosc="1"
font = pygame.font.SysFont("comicsansms", 30)
kto_sie_rusza="Kazio"
Kazio_pozycja=0

while True:
    screen.fill("green")

    #pygame.draw.rect(screen,"red",(30,20,30,30),1)
    #pygame.draw.rect(screen,"red",(60,20,30,30),1)

    szerokosc=50

    pygame.draw.rect(screen,"pink",(15,25,15,15))
    pygame.draw.rect(screen, "red", (15+(Kazio_pozycja*szerokosc), 45, 15, 15))

    for i in range(15):
        pygame.draw.rect(screen, "red", (i*szerokosc, 20, szerokosc, szerokosc), 1)

    for i in range(15):
        pygame.draw.rect(screen, "red", (i*szerokosc, 420, szerokosc, szerokosc), 1)

    for i in range(8):
        pygame.draw.rect(screen, "red", (14*szerokosc, 20+(i*szerokosc), szerokosc, szerokosc), 1)

    pygame.draw.rect(screen,"yellow",(500,500,100,100),10)

    kostka = font.render(kostka_wartosc, True, 'BLUE')
    screen.blit(kostka,(540,525))

    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            kostka_wartosc=str(randint(1,6))
            Kazio_pozycja+=int(kostka_wartosc)



