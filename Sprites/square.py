from Sprites.pieces import *
from Sprites.rook import *
from Sprites.knight import *
from Sprites.bishop import *
from Sprites.queen import *
from Sprites.king import *
from Sprites.pawn import *


#We need to define each square of the board. It must have all the properties of the location, along with
#an occupying piece

#This holds the data of every square on the board
class Square():

    def __init__(self, y, x, color, blocksize,column,row,occupying_piece):
        self.x = x
        self.y = y
        self.centery = self.y+blocksize+45
        self.centerx=self.x+blocksize+45
        self.abs_x = self.x+blocksize
        self.abs_y = self.y+blocksize
        self.color = color
        self.blocksize = blocksize
        self.row = row
        self.column = column
        self.occupying_piece = ""

        #Create the actual rect object that gets drawn
        self.rect = pygame.Rect(x, y, x + blocksize, y + blocksize)
        # Set the last param of 0 to 1 if you want it to be lines only.

    def drawSquare(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)

    def addPiece(self, game,color, piece):
        #here we will work out what to add


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
