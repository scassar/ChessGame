from Classes.pieces import *

class Pawn(Piece):

    def __init__(self, color, x, y, game):
        super().__init__(color, x, y, game)

        self.image = pygame.image.load('Images/'+self.color+'P.svg')
        #self.image = pygame.transform.scale(self.image, (70,70))
        self.image = pygame.transform.scale(self.image, (240,240))

        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        print()

    def legalMoves(self,game,fromSquare):

        legalMoves = []

        if self.color == 'w':

            if (game.squaregrid[fromSquare.row - 1][fromSquare.column].occupying_piece == ''):
                legalMoves.append([fromSquare.row - 1, fromSquare.column])

            if fromSquare.row == 6:
                if (game.squaregrid[fromSquare.row - 2][fromSquare.column].occupying_piece == '' and fromSquare.row == 6 and game.squaregrid[fromSquare.row - 1][fromSquare.column].occupying_piece == ''):
                    legalMoves.append([fromSquare.row - 2, fromSquare.column])

            if fromSquare.column+1 < 8 and fromSquare.row -1 >= 0:
                if game.squaregrid[fromSquare.row-1][fromSquare.column+1].occupying_piece != '' and game.squaregrid[fromSquare.row-1][fromSquare.column+1].occupying_piece.color == 'b':
                    legalMoves.append([fromSquare.row-1, fromSquare.column+1])

            if fromSquare.column-1 >= 0 and fromSquare.row -1 >= 0:
                if game.squaregrid[fromSquare.row-1][fromSquare.column-1].occupying_piece != '' and game.squaregrid[fromSquare.row-1][fromSquare.column-1].occupying_piece.color == 'b':
                    legalMoves.append([fromSquare.row-1, fromSquare.column-1])

            #En Passant Legal move
            if fromSquare.column+1 < 8:
                if game.squaregrid[fromSquare.row][fromSquare.column+1].occupying_piece != '' and game.squaregrid[fromSquare.row][fromSquare.column+1].occupying_piece.color == 'b' and game.squaregrid[fromSquare.row][fromSquare.column+1].occupying_piece.move_count == 1 and game.squaregrid[fromSquare.row][fromSquare.column+1].row == 3:
                    legalMoves.append([fromSquare.row-1, fromSquare.column + 1])

            if fromSquare.column-1 > 0:
                if game.squaregrid[fromSquare.row][fromSquare.column-1].occupying_piece != '' and game.squaregrid[fromSquare.row][fromSquare.column-1].occupying_piece.color == 'b' and game.squaregrid[fromSquare.row][fromSquare.column-1].occupying_piece.move_count == 1 and game.squaregrid[fromSquare.row][fromSquare.column-1].row == 3:
                    legalMoves.append([fromSquare.row-1, fromSquare.column - 1])

        else:

            if (game.squaregrid[fromSquare.row + 1][fromSquare.column].occupying_piece == ''):
                legalMoves.append([fromSquare.row + 1, fromSquare.column])

            if fromSquare.row == 1:
                if (game.squaregrid[fromSquare.row + 2][fromSquare.column].occupying_piece == '' and fromSquare.row == 1 and game.squaregrid[fromSquare.row + 1][fromSquare.column].occupying_piece == ''):
                    legalMoves.append([fromSquare.row + 2, fromSquare.column])

            if fromSquare.column+1 < 8 and fromSquare.row +1 >= 0:
                if game.squaregrid[fromSquare.row+1][fromSquare.column+1].occupying_piece != '' and game.squaregrid[fromSquare.row+1][fromSquare.column+1].occupying_piece.color == 'w':
                    legalMoves.append([fromSquare.row+1, fromSquare.column+1])

            if fromSquare.column-1 >= 0 and fromSquare.row + 1 >= 0:
                if game.squaregrid[fromSquare.row+1][fromSquare.column-1].occupying_piece != '' and game.squaregrid[fromSquare.row+1][fromSquare.column-1].occupying_piece.color == 'w':
                    legalMoves.append([fromSquare.row+1, fromSquare.column-1])

            # En Passant Legal move
            if fromSquare.column+1 < 8:
                if game.squaregrid[fromSquare.row][fromSquare.column+1].occupying_piece != '' and game.squaregrid[fromSquare.row][fromSquare.column+1].occupying_piece.color == 'w' and game.squaregrid[fromSquare.row][fromSquare.column+1].occupying_piece.move_count == 1 and game.squaregrid[fromSquare.row][fromSquare.column+1].row == 4:
                    legalMoves.append([fromSquare.row+1, fromSquare.column + 1])

            if fromSquare.column-1 > 0:
                if game.squaregrid[fromSquare.row][fromSquare.column-1].occupying_piece != '' and game.squaregrid[fromSquare.row][fromSquare.column-1].occupying_piece.color == 'w' and game.squaregrid[fromSquare.row][fromSquare.column-1].occupying_piece.move_count == 1 and game.squaregrid[fromSquare.row][fromSquare.column-1].row == 4:
                    legalMoves.append([fromSquare.row+1, fromSquare.column - 1])

        return legalMoves


