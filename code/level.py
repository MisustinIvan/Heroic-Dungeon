#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, csv

from debug import debug

from settings import *

# ---------------------- CAMERA SHIT -------------------------




class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, player):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - WIDTH/2
        self.offset.y = player.rect.centery - HEIGHT/2

        for sprite in sorted(self.sprites(),key= lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
           





# ------------------------- MAIN SHENANIGANS ---------------



class Level:
    def __init__(self,player):
        self.running_status = True 
        self.display_surface = pygame.display.get_surface()    



# -------------------- PLAYER ----------------------------------------


        self.player = player


# --------------------------- INIT THE GROUPS ---------------------------------------
        


        self.overlap_player_sprites = pygame.sprite.Group()
        self.obstacle_sprites = []
        self.visible_sprites = YSortCameraGroup(self.player)



# ------------------ LOAD THE BACKGROUND FOR THE LEVEL ---------------------------------



        self.background_image = pygame.image.load('../data/maps/map1.png').convert_alpha()
        self.background_image_rect = self.background_image.get_rect()



# ------------------------- CAMERA STUFF ------------------------------------------------



        self.offset = pygame.math.Vector2()



# ---------------------------------------------------------------------------------------


        # self.import_csv_layout('../data/maps/test_level.csv')

    def import_csv_layout(self,path):
        with open(path, newline='\n') as csvfile:
            csvreader = csv.reader(csvfile)
           # TODO - MAKE IT WORK 

    def draw(self):



# ------------------------ DRAW PLAYER AND BACKGROUND --------------------------



        self.display_surface.fill("Black")

        offset_img_rect = self.background_image_rect.topleft - self.offset

        self.display_surface.blit(self.background_image, offset_img_rect)
        self.player.draw(self.offset)



    def update(self):
#   -------------------------------- BACKGROUND IMAGE SHENANIGANS ------------------------------------



        self.offset.x = self.player.rect.centerx - WIDTH/2
        self.offset.y = self.player.rect.centery - HEIGHT/2



#   ----------------------------- OTHER UPDATE STUFF ---------------------------------------------    



        self.player.update()
