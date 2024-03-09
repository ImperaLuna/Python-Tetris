import pygame
import sys

import constants as c

pygame.init()

screen = pygame.display.set_mode((c.FRAME_WIDTH, c.FRAME_HEIGHT))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(c.FRAMERATE)




