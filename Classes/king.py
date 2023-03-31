from Classes.pieces import *

class King(Piece):

    def __init__(self, color, x, y, game):
        super().__init__(color, x, y, game)

        self.image = pygame.image.load('Images/'+self.color+'K.svg')
        self.image = pygame.transform.scale(self.image, (240,240))

        #Determine the position now
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        print()

    def legalMoves(self,game,fromSquare,toSquare):
        print("we are checking moves for a King")
        legalMoves = []

        if self.color == 'w':
            if (abs(toSquare.row - fromSquare.row) < 2 and abs(toSquare.column - fromSquare.column) < 2) and ((toSquare.occupying_piece != '' and toSquare.occupying_piece.color == 'b') or toSquare.occupying_piece == ''):
                legalMoves.append([toSquare.row, toSquare.column])

        if self.color == 'b':
            if (abs(toSquare.row - fromSquare.row) < 2 and abs(toSquare.column - fromSquare.column) < 2) and ((toSquare.occupying_piece != '' and toSquare.occupying_piece.color == 'w') or toSquare.occupying_piece == ''):
                legalMoves.append([toSquare.row, toSquare.column])

        return legalMoves