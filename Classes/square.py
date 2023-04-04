from Classes.pieces import *
from Classes.rook import *
from Classes.knight import *
from Classes.bishop import *
from Classes.queen import *
from Classes.king import *
from Classes.pawn import *
from settings import *
import pygame


#We need to define each square of the board. It must have all the properties of the location, along with
#an occupying piece

#This holds the data of every square on the board
class Square():

    def __init__(self, y, x, color, blocksize,column,row,occupying_piece):
        self.x = x
        self.y = y

        #Mac version is blocksize / 2
        #Windows is blocksize + 45.
        #Eventually need to work out why this is a variance. The mac version makes way more sense.

        #self.centery = self.y+blocksize/2
        self.centery = self.y+blocksize+45
        #self.centerx = self.x+blocksize/2
        self.centerx = self.x+blocksize+45
        self.color = color
        self.blocksize = blocksize
        self.row = row
        self.column = column
        self.occupying_piece = ""
        self.highlighted = False

        #Create the actual rect object that gets drawn. This is x,y,width and height
        self.rect = pygame.Rect(x, y, blocksize, blocksize)
        # Set the last param of 0 to 1 if you want it to be lines only.

    def drawSquare(self, screen):
        if self.highlighted:
            if self.color == BLACK:
                if self.occupying_piece != '' and isinstance(self.occupying_piece,King):
                    pygame.draw.rect(screen, (236,26,26), self.rect, 0)
                else:
                    pygame.draw.rect(screen, (17,102,68), self.rect, 0)
            else:
                if self.occupying_piece != '' and isinstance(self.occupying_piece, King):
                    pygame.draw.rect(screen, (238,91,91), self.rect, 0)
                else:
                    pygame.draw.rect(screen, (85,153,119), self.rect, 0)
        else:
            pygame.draw.rect(screen, self.color, self.rect, 0)


    def addPiece(self, game,color, piece):

        if piece == 'R':
            self.occupying_piece = Rook(color, self.centerx, self.centery, game)
        if piece == 'N':
            self.occupying_piece = Knight(color,  self.centerx, self.centery, game)
        if piece == 'B':
            self.occupying_piece = Bishop(color,  self.centerx, self.centery, game)
        if piece == 'Q':
            self.occupying_piece = Queen(color,  self.centerx, self.centery, game)
        if piece == 'K':
            self.occupying_piece = King(color,  self.centerx, self.centery, game)
        if piece == 'P':
            self.occupying_piece = Pawn(color,  self.centerx, self.centery, game)
