from Classes.pieces import *

class King(Piece):

    def __init__(self, color, x, y, game):
        super().__init__(color, x, y, game)

        self.image = pygame.image.load('Images/'+self.color+'K.svg')
        self.image = pygame.transform.scale(self.image, (70,70))
        #self.image = pygame.transform.scale(self.image, (240,240))

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

        moves = [
            (0, -1),  # north
            (1, -1),  # ne
            (1, 0),  # east
            (1, 1),  # se
            (0, 1),  # south
            (-1, 1),  # sw
            (-1, 0),  # west
            (-1, -1),  # nw
        ]

        for move in moves:
            new_pos = [fromSquare.row + move[0], fromSquare.column + move[1]]
            if (
                    new_pos[0] < 8 and
                    new_pos[0] >= 0 and
                    new_pos[1] < 8 and
                    new_pos[1] >= 0
            ):
                legalMoves.append(new_pos)

        return legalMoves