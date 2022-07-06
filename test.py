#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1920,1200))
clock = pygame.time.Clock()

image = pygame.image.load("data/maps/map1.png").convert_alpha()
image_rect = image.get_rect()

counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(image, image_rect)
    pygame.display.flip()
    print(counter)
    counter += 1
    clock.tick(30)
