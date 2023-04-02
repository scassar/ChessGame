from Classes.pieces import *

class Pawn(Piece):

    def __init__(self, color, x, y, game):
        super().__init__(color, x, y, game)

        self.image = pygame.image.load('Images/'+self.color+'P.svg')
        self.image = pygame.transform.scale(self.image, (70,70))
       # self.image = pygame.transform.scale(self.image, (240,240))

        #Determine the position now
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        print()

    def legalMoves(self,game,fromSquare,toSquare):

        legalMoves = []

        if self.color == 'w':

            if (toSquare.occupying_piece == ''):
                legalMoves.append([fromSquare.row - 1, fromSquare.column])

            if (fromSquare.row == 6 and toSquare.occupying_piece == ''):
                legalMoves.append([fromSquare.row - 2, fromSquare.column])
                print('move added 2')

            if toSquare.row == fromSquare.row - 1 and abs(
                    toSquare.column - fromSquare.column) == 1 and toSquare.occupying_piece != '' and toSquare.occupying_piece.color == 'b':
                legalMoves.append([toSquare.row, toSquare.column])

        else:
            if (toSquare.occupying_piece == ''):
                legalMoves.append([fromSquare.row + 1, fromSquare.column])

            if (fromSquare.row == 1 and toSquare.occupying_piece == ''):
                legalMoves.append([fromSquare.row + 2, fromSquare.column])

            if toSquare.row == fromSquare.row + 1 and abs(
                    toSquare.column - fromSquare.column) == 1 and toSquare.occupying_piece != '' and toSquare.occupying_piece.color == 'w':
                legalMoves.append([toSquare.row, toSquare.column])

        return legalMoves


