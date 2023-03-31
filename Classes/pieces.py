import pygame
import math
from settings import *
from enum import Enum
vec = pygame.math.Vector2

#This enum just maps the image files to be used for a given piece on the board

# Here we want the code to control the piece. By default it will be part of inheting from pygame Sprite object. You
# want to override the rect, image and update() functions
class Piece(pygame.sprite.Sprite):

    def __init__(self, color, x,y, game):
        # Call the parent class (Sprite) constructor

        self.groups = game.all_sprites
        self.layers = 1
        self.game = game
        self.color = color
        self.x = x
        self.y=y
        self.pos = vec()

        #Call to the super class init function. What does this do?
        pygame.sprite.Sprite.__init__(self, self.groups)

    def update(self):
        print()



    def returnSelected(self,x,y):
        return


   # No longer needed in the new method
    def determineXY(self):
        xrow = self.tile / 8
        xtile = self.tile % 8
        if xrow <= 1:
            self.xpos = self.tile * 90 - 45
            self.ypos = 45
        elif 1 <= xrow <= 2:
            if xtile == 0:
                self.xpos = (8 * 90) - 45
                self.ypos = 2 * 90 - 45
            else:
                self.xpos = (xtile * 90) - 45
                self.ypos = 2 * 90 - 45
        elif 2 < xrow <= 3:
            if xtile == 0:
                self.xpos = (8 * 90) - 45
                self.ypos = 3 * 90 - 45
            else:
                self.xpos = (xtile * 90) - 45
                self.ypos = 3 * 90 - 45
        elif 3 < xrow <= 4:
            if xtile == 0:
                self.xpos = (8 * 90) - 45
                self.ypos = 4 * 90 - 45
            else:
                self.xpos = (xtile * 90) - 45
                self.ypos = 4 * 90 - 45
        elif 4 < xrow <= 5:
            if xtile == 0:
                self.xpos = (8 * 90) - 45
                self.ypos = 5 * 90 - 45
            else:
                self.xpos = (xtile * 90) - 45
                self.ypos = 5 * 90 - 45
        elif 5 < xrow <= 6:
            if xtile == 0:
                self.xpos = (8 * 90) - 45
                self.ypos = 6 * 90 - 45
            else:
                self.xpos = (xtile * 90) - 45
                self.ypos = 6 * 90 - 45
        elif 6 < xrow <= 7:
            if xtile == 0:
                self.xpos = (8 * 90) - 45
                self.ypos = 7 * 90 - 45
            else:
                self.xpos = (xtile * 90) - 45
                self.ypos = 7 * 90 - 45
        elif 7 < xrow <= 8:
            if xtile == 0:
                self.xpos = (8 * 90) - 45
                self.ypos = 8 * 90 - 45
            else:
                self.xpos = (xtile * 90) - 45
                self.ypos = 8 * 90 - 45
        return (self.xpos, self.ypos)
