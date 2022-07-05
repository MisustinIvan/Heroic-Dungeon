#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, csv

class Level:
    def __init__(self):
        self.running_status = True 
        self.display_surface = pygame.display.get_surface()    

        self.import_csv_layout('../data/maps/test_level.csv')

    def import_csv_layout(self,path):
        with open(path, newline='\n') as csvfile:
            csvreader = csv.reader(csvfile)
            for shit in csvreader:
                for shus in shit:
                    print(shus)

    def draw(self):
        pass


    def update(self):
        pass
