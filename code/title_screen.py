#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys


# ---------------------------------------- WHAT IS THIS SHIT FOR? -> DRAW A MAIN MENU ON SCREEN(there will be some shit written on it) - allows to start or quit the torture(game) -------------------


class TitleScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.background_image = pygame.image.load('../graphics/background.png').convert_alpha()

    def show(self):
        running = True
        while running:
            img_rect = self.background_image.get_rect()
            self.display_surface.blit(self.background_image,img_rect)
    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                        print("sucker")
# -------------------------------------------------------- SOME BASIC LOGIC HERE, THIS SHALL NOT BE TOUCHED FOR THE REST OF THE PROJECT(mby i will ad some music to the title screen)-------------------
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.flip()            
