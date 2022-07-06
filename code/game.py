#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys
from settings import *
from level import Level
from title_screen import TitleScreen
from player import Player

class Game:
    def __init__(self):

        # ------------- INITIALIZE THE BASIC SCREEN -----------------

        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Heroic Dungeon")
        
        self.player = Player()

        self.level_running = False

    def run(self):
        title_screen = TitleScreen()
        title_screen.show()
        while True:
        # --------------- EVENT LOOP --------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
        # ----------- IF EVENT QUIT, KILL THE PROGRAM ---------------
                    pygame.quit()
                    sys.exit()

        # ------------- DRAW AND UPDATE THE LEVEL -------------------
            

            if self.level_running == False:
                self.level = Level(self.player)
                self.level_running = True
            else:
                self.level.update()
                self.level.draw()

            self.level_running = self.level.running_status

        # --------------- DEBUGAGE ------------------------


        # ---------------- UPDATE THE GAME 60 TIMES PER SECOND -----------------
            pygame.display.flip()
            self.clock.tick(FPS)
