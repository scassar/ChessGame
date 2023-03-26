import pygame
import math
from settings import *
from enum import Enum

vec = pygame.math.Vector2

#This enum just maps the image files to be used for a given piece on the board
class PiecesList(Enum):
    BPAWN = "bP.svg"
    BKNIGHT = "bK.svg"
    BROOK = "bR.svg"
    BBISHOP = "bB.svg"
    BQUEEN = "bQ.svg"
    BKING = "bK.svg"
    WPAWN = "wP.svg"
    WKNIGHT = "wK.svg"
    WROOK = "wR.svg"
    WBISHOP = "wB.svg"
    WQUEEN = "wQ.svg"
    WKING = "wK.svg"

# Here we want the code to control the piece. By default it will be part of inheting from pygame Sprite object.
class Piece(pygame.sprite.Sprite):

    def __init__(self, color, width, height, tile, type, game):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.groups = game.all_sprites
        self.layers = 1
        self.game = game

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = width
        self.color = color
        self.height = height
        self.tile = tile
        self.type = type

        self.image = pygame.image.load('Images/'+self.type.value)
        self.image = pygame.transform.scale(self.image, (70,70))
        #print('Images/'+self.type.value)

        #Determine the position now

        self.pos = vec(100,100)
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        #We just need a way to calculte starting positions based on tile location

        self.rect.center = self.determineXY()

    def update(self):
        #We will put code here for what happens when the pieces move
        print("entering update function for sprites")

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
