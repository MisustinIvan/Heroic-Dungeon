#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
pygame.init()

def debug(data, x = 10, y = 10):
    font = pygame.font.Font(None,30)
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(data),True,'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
