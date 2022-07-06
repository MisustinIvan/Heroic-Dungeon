#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Player():
    def __init__(self):
        self.image = pygame.image.load("../graphics/Tileset/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pygame.math.Vector2()
        
        self.display_surface = pygame.display.get_surface()


        self.direction = pygame.math.Vector2()
        self.speed = 10 


    def draw(self,offset):
        offset_rect = self.rect.topleft - offset
        self.display_surface.blit(self.image, offset_rect)

    def update(self):
        self.input()
        self.move()


    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0


        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0



    def move(self):

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
