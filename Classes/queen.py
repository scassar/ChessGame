from Classes.pieces import *

class Queen(Piece):

    def __init__(self, color, x, y, game):
        super().__init__(color, x, y, game)

        self.image = pygame.image.load('Images/'+self.color+'Q.svg')
        #self.image = pygame.transform.scale(self.image, (240,240))
        self.image = pygame.transform.scale(self.image, (70,70))

        #Determine the position now
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        print()

    def legalMoves(self,game,fromSquare,toSquare):

        print("we are checking moves for a Queen")
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

        for y in range(fromSquare.row):
            legalMoves.append([y, fromSquare.column])

            # move south

        for y in range(fromSquare.row + 1, 8):
            legalMoves.append([y, fromSquare.column])

            # move east

        for x in range(fromSquare.column + 1, 8):
            legalMoves.append([fromSquare.row, x])

            # move west

        for y in range(fromSquare.column):
            legalMoves.append([fromSquare.row, y])


        return legalMoves