from Classes.pieces import *
import pygame

class Rook(Piece):

    def __init__(self, color, x, y, game):

        #we can call the parent class init to set our state
        super().__init__(color, x, y, game)

        self.image = pygame.image.load('Images/'+self.color+'R.svg')
        #self.image = pygame.transform.scale(self.image, (240,240))
        self.image = pygame.transform.scale(self.image, (70,70))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        print()

    def legalMoves(self,game,fromSquare,toSquare):

        legalMoves = []

        #moe north

        for y in range(fromSquare.row+1):
            if game.squaregrid[fromSquare.row - y][fromSquare.column].occupying_piece != '':
                if game.squaregrid[fromSquare.row - y][fromSquare.column] != fromSquare:
                     legalMoves.append([fromSquare.row - y, fromSquare.column])
                     break
            legalMoves.append([fromSquare.row - y, fromSquare.column])

        #move south
        for y in range(fromSquare.row+1, 8):
            if game.squaregrid[y][fromSquare.column].occupying_piece != '':
                if game.squaregrid[y][fromSquare.column] != fromSquare:
                    legalMoves.append([y, fromSquare.column])
                    break
            legalMoves.append([y, fromSquare.column])


        #move east

        for x in range(fromSquare.column + 1, 8):
            if game.squaregrid[fromSquare.row][x].occupying_piece != '':
                if game.squaregrid[fromSquare.row][x] != fromSquare:
                    legalMoves.append([fromSquare.row, x])
                    break
            legalMoves.append([fromSquare.row, x])


        #move west

        for y in range(fromSquare.column + 1):
            if game.squaregrid[fromSquare.row][fromSquare.column-y].occupying_piece != '':
                if game.squaregrid[fromSquare.row][fromSquare.column-y] != fromSquare:
                    legalMoves.append([fromSquare.row, fromSquare.column-y])
                    break
            legalMoves.append([fromSquare.row, fromSquare.column-y])


        print(legalMoves)

        invalid_move = True
        for moves in legalMoves:
            if moves[0] == toSquare.row and moves[1] == toSquare.column:
                print (moves[0], moves[1])
                invalid_move = False

                break

        if invalid_move or (toSquare.occupying_piece != '' and toSquare.occupying_piece.color == self.color):
            print('illegal move')
            legalMoves=[]


        return legalMoves









