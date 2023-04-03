# Simple pygame program
import pygame
# Import and initialize the pygame library
from Classes.square import *
import time

#Manage the overall game state. IF we dont use this we have to define everything as global which isnt as nice.

class Game():

    def __init__(self):
        # initialise the module
        pygame.init()
        pygame.display.set_caption(GAMENAME)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))

    def new_game(self):
        self.selected_piece = None
        self.selected_square = None
        self.white_king_square = None
        self.black_king_square = None
        self.game_over = False
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.turn = 'w'
        # representation of the current board / board start
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

        # self.board = [
        #     ['--', '--', '--', '--', 'bK', '--', '--', '--'],
        #     ['--', '--', '--', '--', '--', '--', '--', '--'],
        #     ['--', '--', '--', '--', '--', '--', '--', '--'],
        #     ['--', '--', '--', '--', '--', '--', '--', '--'],
        #     ['--', '--', '--', '--', '--', '--', '--', '--'],
        #     ['--', '--', '--', '--', '--', '--', '--', '--'],
        #     ['--', '--', '--', '--', '--', '--', '--', '--'],
        #     ['wR', 'wR', '--', '--', 'wK', '--', '--', '--'],
        # ]

        self.squaregrid = [[], [], [], [], [], [], [], []]

        self.create_board()
        self.create_pieces()

        self.running()

    def toggle_turn(self):
        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'

    def create_board(self):
        # Create all the square objects first
        blockSize = 90
        color = WHITE

        column = 0

        for x in range(0, WIDTH, blockSize):  # x coordinate
            color = self.flip_color(color)
            row = 0
            column = column + 1

            for y in range(0, HEIGHT, blockSize):  # y coordinate
                # Now we alternate the colours of the blocks
                color = self.flip_color(color)

                # Create the first square object in a 2d list
                # Also add in the occupying piece for the start

                self.squaregrid[column - 1].append(Square(x, y, color, blockSize, row, column - 1, ''))
                row = row + 1

    def create_pieces(self):
        #Now we add each piece to the board squares.

        for x in range(8):
            for y in range(8):

                board_value = self.board[x][y]
                attributes = self.determine_piece(board_value)
                colour = attributes[0]
                piece_code = attributes[1]

                if piece_code != '--':
                    self.squaregrid[x][y].addPiece(self,colour,piece_code)
                    if colour == 'w' and piece_code == 'K':
                        self.white_king_square = self.squaregrid[x][y]
                        #print(f'White king is at location {x} {y}')
                    elif colour == 'b' and piece_code == 'K':
                        self.black_king_square = self.squaregrid[x][y]
                        #print(f'Black king is at location {x} {y}')


    def determine_piece(self, piece):
        #This function will return back what piece object based on the letters in the board array for setup

        values = piece.split()
        color = values[0][0]
        occupying_piece = values[0][1]

        if piece == '--':
            return ['--','--']
        else:

            return [color,occupying_piece]

    #Once we have the initial list of squares, now we can loop and draw them all
    def draw_board(self):

        blockSize = 90 #Set the size of the grid block

        for x in range(8):
            for y in range(8):
                self.squaregrid[x][y].drawSquare(self.screen)

    def flip_color(self, color):

        WHITE = (240,240,240)
        BLACK = (30,30,30)
        if not color or color == WHITE:
            color = BLACK
        else:
            color = WHITE
        return color

    def draw(self):

        self.draw_board()

        # Draw the pieces on the screen.
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def update(self):
        #self.all_sprites.update()
        return

    #Function returns the square object we have clicked on
    def locate_square(self,pos):
        for i in range(8):
            for z in range(8):
                if (self.squaregrid[i][z].rect.collidepoint(pos)):
                        return self.squaregrid[i][z]

    #This must return an array of square objects that are legal objects to move
    def find_legal_moves(self, fromSquare, toSquare):

        legal_moves = fromSquare.occupying_piece.legalMoves(self,fromSquare,toSquare)

        print(f'the legal moves are  {legal_moves}')
        return legal_moves #Array list of row,columns that can be used


    def highlight_squares(self,highlight_list):
        for x in highlight_list:
            row = x[0]
            column = x[1]
            if self.squaregrid[row][column].highlighted:
                self.squaregrid[row][column].highlighted = False
            else:
                self.squaregrid[row][column].highlighted = True

    def find_illegal_moves(self, piece):
        #Return if after making a move there is someone who can see the king.
        #Piece passed in is the selected one
        legal_moves = []
        legal_moves_temp=[]

        for x in range(8):
            for y in range(8):
                if (self.squaregrid[x][y].occupying_piece != '' and self.squaregrid[x][y].occupying_piece.color != piece.color): #Get the opposite color. We check the square against passed color and want a different value
                    if piece.color == 'w':
                        legal_moves_temp = self.squaregrid[x][y].occupying_piece.legalMoves(self, self.squaregrid[x][y], self.white_king_square)  #returna a list
                        #print(f'Checking illegal moves for {self.squaregrid[x][y].occupying_piece.color},{self.white_king_square.row}, {self.white_king_square.column}')
                    else:
                        legal_moves_temp = self.squaregrid[x][y].occupying_piece.legalMoves(self, self.squaregrid[x][y], self.black_king_square)
                        #print(f'Checking illegal moves for {self.squaregrid[x][y].occupying_piece.color}, {self.black_king_square.row}, {self.black_king_square.column}')

                #Get legal moves for the other side.
                legal_moves = legal_moves + legal_moves_temp

        #check if the king is now a target from the other teams moves.

        illegal = False

        for move in legal_moves:
            if piece.color == 'w':
                if move[0] == self.white_king_square.row and move[1] == self.white_king_square.column:
                    illegal = True

            else:
                if move[0] == self.black_king_square.row and move[1] == self.black_king_square.column:
                    illegal = True

        return illegal

    #Working on this logic
    def is_checkmate(self, square):

        #Loop through for each king and check if all moves are illegal
        checkmate = False
        print(f'the white king is now at {self.white_king_square.row}, {self.white_king_square.column}')
        print(f'the white king piece now at {self.white_king_square.occupying_piece}')

        if self.turn == 'b':  #Do this if the last piece moved was black

            checkmate = True
            legal_moves = []
            king_square = self.squaregrid[self.white_king_square.row][self.white_king_square.column]

            if square.occupying_piece != '':
                legal_moves = self.find_legal_moves(king_square, square)  #Get all moves the white king can make

            if len(legal_moves) == 0:
                checkmate = False

            for move in legal_moves:
                #for each move, move the king and see if its legal

                backup_king_square = self.squaregrid[self.white_king_square.row][self.white_king_square.column]
                backup_king_piece = self.squaregrid[self.white_king_square.row][self.white_king_square.column].occupying_piece

                temp_square = self.squaregrid[move[0]][move[1]]
                temp_square_piece = self.squaregrid[move[0]][move[1]].occupying_piece


                #Move the king and update the previous square to blank
                self.squaregrid[move[0]][move[1]].occupying_piece = self.white_king_square.occupying_piece
                self.squaregrid[self.white_king_square.row][self.white_king_square.column].occupying_piece = ''
                self.white_king_square = self.squaregrid[move[0]][move[1]]


                illegal = self.find_illegal_moves(self.white_king_square.occupying_piece)



                #revert back move now
                #self.squaregrid[move[0]][move[1]].occupying_piece = temp_square.occupying_piece


                self.squaregrid[backup_king_square.row][backup_king_square.column].occupying_piece = self.squaregrid[move[0]][move[1]].occupying_piece
                self.squaregrid[move[0]][move[1]].occupying_piece = temp_square_piece
                self.white_king_square = backup_king_square

                if not illegal:
                    checkmate = False
                    print('No Checkmate found yet')
                    break
        elif self.turn == 'w':  #Do this if the last piece moved was black

            checkmate = True
            legal_moves = []

            king_square = self.squaregrid[self.black_king_square.row][self.black_king_square.column]

            if square.occupying_piece != '':
                legal_moves = self.find_legal_moves(king_square, square)

            if len(legal_moves) == 0:
                checkmate = False

            for move in legal_moves:

                backup_king_square = self.squaregrid[self.black_king_square.row][self.black_king_square.column]
                temp_square_piece = self.squaregrid[move[0]][move[1]].occupying_piece


                #Move the king and update the previous square to blank
                self.squaregrid[move[0]][move[1]].occupying_piece = self.black_king_square.occupying_piece
                self.squaregrid[self.black_king_square.row][self.black_king_square.column].occupying_piece = ''
                self.black_king_square = self.squaregrid[move[0]][move[1]]

                illegal = self.find_illegal_moves(self.black_king_square.occupying_piece)

                self.squaregrid[backup_king_square.row][backup_king_square.column].occupying_piece = self.squaregrid[move[0]][move[1]].occupying_piece
                self.squaregrid[move[0]][move[1]].occupying_piece = temp_square_piece
                self.black_king_square = backup_king_square

                if not illegal:
                    checkmate = False
                    break

        return checkmate


    def handle_click(self,pos):
        clicked_square = self.locate_square(pos)

        if (clicked_square.occupying_piece == '' and self.selected_piece is None):
            print("Not a selectable square")
            return

        #Enter this loop when selecting a piece. Select the square and piece we want to target first.
        if self.selected_piece is None:
            if (clicked_square.occupying_piece != '' and clicked_square.occupying_piece.color == self.turn):
                self.selected_piece = clicked_square.occupying_piece
                self.selected_square = clicked_square

                #highlight_moves = self.find_legal_moves(self.selected_square, clicked_square)
                #update all squares in highlight_moves array
                #self.highlight_squares(highlight_moves)

        else:
            legal_moves = self.find_legal_moves(self.selected_square, clicked_square)

            #highlight_moves = legal_moves

            if len(legal_moves) == 0:
                self.selected_piece = None
                self.selected_square = None

            #This is where we make the actual moves. we want to reduce the list of legal moves first
            for move in legal_moves:
                if move[0] == clicked_square.row and move[1] == clicked_square.column:

                    #Here we matched a legal move. For this givem move, we need to see if after making it,
                    #the game would result in a check

                    if (clicked_square.occupying_piece != '' and self.selected_square != clicked_square):
                        clicked_square.occupying_piece.rect.center = (-100,-100)

                #Check for legal move. What we need to know here is the from square, peice and target square

                    if self.selected_square.occupying_piece.color == 'w' and isinstance(self.selected_square.occupying_piece,King):
                        self.white_king_square = clicked_square

                    elif self.selected_square.occupying_piece.color == 'b' and isinstance(self.selected_square.occupying_piece,King):
                        self.black_king_square = clicked_square

                    backup_piece = self.selected_square.occupying_piece
                    backup_square = self.selected_square
                    backup_clicked_square = clicked_square
                    backup_clicked_piece = clicked_square.occupying_piece

                    # Set the new square = to the selected square and update the piece.
                    clicked_square.occupying_piece = self.selected_piece
                    self.selected_piece.rect.center = (clicked_square.centerx, clicked_square.centery)
                    self.selected_square.occupying_piece = ''

                #Now check if that move was illegal. Basically return true if someone can now touch the king
                #Pass the piece that was updated to the new spot (the colour of the turn

                    illegal = self.find_illegal_moves(backup_piece)

                    print(f'Is this move illegal? {illegal}')

                    if illegal:  #revert back

                        self.toggle_turn()
                        clicked_square.occupying_piece = backup_clicked_piece
                        if clicked_square.occupying_piece != '':
                            clicked_square.occupying_piece.rect.center = (backup_clicked_square.centerx, backup_clicked_square.centery)

                        self.selected_square.occupying_piece = backup_piece
                        if self.selected_square.occupying_piece != '':
                            self.selected_square.occupying_piece.rect.center = (backup_square.centerx, backup_square.centery)

                        #Revet global king position
                        if self.selected_square.occupying_piece.color == 'w' and isinstance(self.selected_square.occupying_piece, King):
                            self.white_king_square = backup_square

                        elif self.selected_square.color == 'b' and isinstance(self.selected_square.occupying_piece,King):
                            self.black_king_square = backup_square
                    else:
                        #check for checkmate

                        check_mate = self.is_checkmate(clicked_square)

                        if check_mate:
                            if self.turn == 'w':
                                highlight_list = [[self.black_king_square.row,self.black_king_square.column]]
                            else:
                                highlight_list = [[self.black_king_square.row, self.black_king_square.column]]

                            print(f'the highlight list is {highlight_list}')
                            self.highlight_squares(highlight_list)

                    self.selected_piece = None
                    self.selected_square = None
                    self.toggle_turn()


    def running(self):

        # Set up the drawing window
        # We are going for W=1280, H=720
        screen = pygame.display.set_mode([HEIGHT, WIDTH])

        # Run until the user asks to quit
        running = True
        while running:

            self.clock.tick(60)
            pos = pygame.mouse.get_pos()
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(pos)

            # Fill the background with white
            screen.fill((255, 255, 255))

            # Draw a solid blue circle in the center

            self.update()

            #This will mark the player grid of squares
            self.draw()

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()


#Here we start the game

game = Game()
game.new_game()