import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False 

while not done:
    for event in pygame.event.get():
        done = True
pygame.draw.rect(screen,(233,0,0), pygame.Rect(30,50,100,60))

pygame.display.flip()