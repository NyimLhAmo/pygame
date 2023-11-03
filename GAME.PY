import pygame
# from pygame.local import *

pygame.init()
clock = pygame.time.Clock()
FPS = 60


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Momo jump")

Momo = pygame.Rect((300, 250, 50, 50))

bg = pygame.image.load("pygame\GAME\dog.png")


running = True
while running:
    clock.tick(FPS)  

    screen.blit(bg, (0, 0))     

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,(255, 0, 0), Momo)

    

    key = pygame.key.get_pressed()
    if key[pygame.K_z] == True:
        Momo.move(-1, 0)
    elif key[pygame.K_x] == True:
        Momo.move_ip(1, 0)
    elif key[pygame.K_n] == True:
        Momo.move_ip(0, -1)  
    elif key[pygame.K_m] == True:
        Momo.move_ip(0, 1)          
     
     #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()