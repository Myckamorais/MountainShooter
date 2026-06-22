#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame


class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        pygame.init()
        print('Satup Start')
        window = pygame.display.set_mode((600, 480))
        print('Satup Finish')

        print('Loop Start')
        while True:
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
