import pygame
from sys import exit
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('my game')
width = 800
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
test_surf = pygame.Surface((400, 900))
test_surf.fill('White')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.blit(test_surf, (0,0))
    pygame.display.update()
    clock.tick(60)