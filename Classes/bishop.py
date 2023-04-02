from Classes.pieces import *

class Bishop(Piece):

    def __init__(self, color, x, y, game):
        super().__init__(color, x, y, game)

        self.image = pygame.image.load('Images/'+self.color+'B.svg')
        self.image = pygame.transform.scale(self.image, (70,70))
        #self.image = pygame.transform.scale(self.image, (240,240))

        #Determine the position now
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    #return array of legal moves
    def legalMoves(self,game,fromSquare,toSquare):

        print("we are checking moves for a Bishop")
        legalMoves = []
        # We need to calculate the movement for the bishop

        for i in range(1, 8):
            if fromSquare.row + i > 7 or fromSquare.column - i < 0:
                break
            legalMoves.append([fromSquare.row + i, fromSquare.column - i])

        for i in range(1, 8):
            if fromSquare.row + i > 7 or fromSquare.column + i > 7:
                break
            legalMoves.append([fromSquare.row + i, fromSquare.column + i])

        for i in range(1, 8):
            if fromSquare.row - i < 0 or fromSquare.column + i > 7:
                break
            legalMoves.append([fromSquare.row - i, fromSquare.column + i])

        for i in range(1, 8):
            if fromSquare.row - i < 0 or fromSquare.column - i < 0:
                break
            legalMoves.append([fromSquare.row - i, fromSquare.column - i])

        return legalMoves


