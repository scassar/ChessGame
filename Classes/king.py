from Classes.pieces import *

class King(Piece):

    def __init__(self, color, x, y, game):
        super().__init__(color, x, y, game)

        self.image = pygame.image.load('Images/'+self.color+'K.svg')
        #self.image = pygame.transform.scale(self.image, (70,70))
        self.image = pygame.transform.scale(self.image, (240,240))

        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        print()

    def handle_castle(self,game,from_square,clicked_square):
        #here we will simply check if the king can castle. Lets just implement basic castle
        backup_rook = self.squaregrid[self.white_king_square.row][self.white_king_square.column + 3]
        self.white_king_square = clicked_square
        self.squaregrid[self.white_king_square.row][self.white_king_square.column + 3]

        return

    def legalMoves(self,game,fromSquare):
        #print("we are checking moves for a King")
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
            and ((game.squaregrid[fromSquare.row + move[0]][fromSquare.column + move[1]].occupying_piece != '' and game.squaregrid[fromSquare.row + move[0]][fromSquare.column + move[1]].occupying_piece.color != self.color) or game.squaregrid[fromSquare.row + move[0]][fromSquare.column + move[1]].occupying_piece == '')):

                legalMoves.append(new_pos)

        #Check for castle and add legal move if there is no blocking pieces

        # if self.move_count == 0:
        #      #Right side rook
        #      if game.squaregrid[fromSquare.row][fromSquare.column+3].occupying_piece.move_count == 0:
        #
        #         if game.squaregrid[fromSquare.row][fromSquare.column+2].occupying_piece == '' and game.squaregrid[fromSquare.row][fromSquare.column + 1].occupying_piece == '':
        #             #This means we can castle right
        #
        #             legalMoves.append([fromSquare.row, fromSquare.column+2])
        #
        # if game.squaregrid[fromSquare.row][fromSquare.column-4].occupying_piece.move_count == 0:
        #
        #     if game.squaregrid[fromSquare.row][fromSquare.column - 3].occupying_piece == '' and \
        #         game.squaregrid[fromSquare.row][fromSquare.column - 2].occupying_piece == '' and game.squaregrid[fromSquare.row][fromSquare.column - 1].occupying_piece == '':
        #         # This means we can castle left
        #
        #         legalMoves.append([fromSquare.row, fromSquare.column - 2])

        return legalMoves