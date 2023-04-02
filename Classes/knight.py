from Classes.pieces import *

class Knight(Piece):

    def __init__(self, color, x, y, game):
        super().__init__(color, x, y, game)
        #add sprite to the game all_sprites group


        self.image = pygame.image.load('Images/'+self.color+'N.svg')
        self.image = pygame.transform.scale(self.image, (240,240))
        #self.image = pygame.transform.scale(self.image, (70,70))

        #Determine the position now
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        print()


    def legalMoves(self,game,fromSquare,toSquare):
        legalMoves = []

        moves = [
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2)
        ]

        for move in moves:
            new_pos = [fromSquare.row + move[0], fromSquare.column + move[1]]

            if (
                    new_pos[0] < 8 and
                    new_pos[0] >= 0 and
                    new_pos[1] < 8 and
                    new_pos[1] >= 0
            and ((toSquare.occupying_piece != '' and toSquare.occupying_piece.color != self.color) or toSquare.occupying_piece == '')):
                legalMoves.append(new_pos)

        return legalMoves