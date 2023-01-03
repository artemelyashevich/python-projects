import pygame
from datetime import datetime

RES = WIDTH, HEIGHT = 800, 500

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Tahoma', 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    surface.fill(pygame.Color('black'))
    time = datetime.now()
    time_render = font.render(f'{time:%H:%M:%S}', True, pygame.Color('green'), pygame.Color('black'))
    surface.blit(time_render, (100,150))

    pygame.display.flip()
    clock.tick(10)