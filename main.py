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

    #Called to refresh and start a new game
    def new_game(self):
        self.selected_piece = None
        self.selected_square = None
        self.white_king_square = None
        self.black_king_square = None
        self.game_over = False
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.turn = 'w'
        #representation of the current board / board start
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
        #      ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        #      ['bP', 'bP', 'bP', 'bP', '--', 'bP', 'bP', 'bP'],
        #      ['--', '--', '--', '--', '--', '--', '--', '--'],
        #      ['--', '--', '--', '--', '--', '--', '--', '--'],
        #      ['--', '--', '--', '--', '--', '--', '--', '--'],
        #      ['--', '--', '--', '--', '--', '--', '--', '--'],
        #      ['wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP'],
        #      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        #  ]

        self.squaregrid = [[], [], [], [], [], [], [], []]

        self.create_board()
        self.create_pieces()
        self.running()

    #Change the current turn of the game
    def toggle_turn(self):
        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'

    #Create all squaregrid square objects
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

    #Setup pieces on the board for given self.board setup in __init__
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

    # This function will return back what piece object based on the letters in the board array for setup
    def determine_piece(self, piece):


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

    #Pass in a color (white / black) and result is the opposite
    def flip_color(self, color):

        WHITE = (240,240,240)
        BLACK = (30,30,30)
        if not color or color == WHITE:
            color = BLACK
        else:
            color = WHITE
        return color

    #Main draw function called from main game loop
    def draw(self):

        self.draw_board()

        # Draw the pieces on the screen.
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    #Takes in a mouse position on click, and determines the selected square within squaregrid.
    def locate_square(self,pos):
        for i in range(8):
            for z in range(8):
                if (self.squaregrid[i][z].rect.collidepoint(pos)):
                        return self.squaregrid[i][z]

    #This must return an array of square objects that are legal objects to move. Format Square
    def find_legal_moves(self, fromSquare):

        legal_moves = fromSquare.occupying_piece.legalMoves(self,fromSquare)

        return legal_moves

    #Pass in a list of legal moves, and these will be highlighted. Format [[1,1,2,2]
    def highlight_squares(self,highlight_list):
        for x in highlight_list:
            row = x[0]
            column = x[1]
            if self.squaregrid[row][column].highlighted:
                self.squaregrid[row][column].highlighted = False
            else:
                self.squaregrid[row][column].highlighted = True

    #Returns entire list of moves from the opposite team to the passed in color
    def check_all_moves_opp_color(self, color):

        legal_moves = []
        legal_moves_temp=[]

        for x in range(8):
            for y in range(8):
                if (self.squaregrid[x][y].occupying_piece != '' and self.squaregrid[x][y].occupying_piece.color != color): #Get the opposite color. We check the square against passed color and want a different value
                    if color == 'w':
                        legal_moves_temp = self.squaregrid[x][y].occupying_piece.legalMoves(self, self.squaregrid[x][y])
                    else:
                        legal_moves_temp = self.squaregrid[x][y].occupying_piece.legalMoves(self, self.squaregrid[x][y])

                legal_moves = legal_moves + legal_moves_temp

        return legal_moves

    #Function is called when a move is made, and evaluates whether the current position on the board is illegal.
    #Checks if any piecve from the opposite team can currently see any of the kings after move.
    def find_illegal_moves(self, piece):

        legal_moves = self.check_all_moves_opp_color(piece.color)

        illegal = False

        for move in legal_moves:
            if piece.color == 'w':
                if move[0] == self.white_king_square.row and move[1] == self.white_king_square.column:
                    illegal = True
            else:
                if move[0] == self.black_king_square.row and move[1] == self.black_king_square.column:
                    illegal = True

        return illegal

    #Takes in the square of the last moved piece. Then checks the legal moves of that piece and if it targets the enemy king, then the result is true
    def is_in_check(self,square):
        check = False

        if self.turn == 'w':
            king_square = self.black_king_square

        elif self.turn == 'b':
            king_square = self.white_king_square

        legal_moves = self.find_legal_moves(square)

        for moves in legal_moves:
            if moves[0] == king_square.row and moves[1] == king_square.column:
                check = True

        return check

    #Checkmate function to confirm if the game is to end.
    #Takes an arguement of the last square that was moved, and will return if the enemy king can no longer make any moves.

    def is_checkmate(self, square):

        checkmate = False

        #Confirm first if the opposite king is in check as result of the move
        check = self.is_in_check(square)

        if check:

            if self.turn == 'b':
                king_square = self.squaregrid[self.white_king_square.row][self.white_king_square.column]
            elif self.turn == 'w':
                king_square = self.squaregrid[self.black_king_square.row][self.black_king_square.column]

            self.highlight_squares([[king_square.row, king_square.column]])


            checkmate = True


            #Loop through all squares on the board.
            for x in range(8):
                for y in range(8):

                    #We will check the legal moves of all pieces on the team where the check as occured. This is to identify if there is atleast one legal move.

                    if (self.squaregrid[x][y].occupying_piece != '' and self.squaregrid[x][y].occupying_piece.color == king_square.occupying_piece.color and checkmate == True):  # Loop all pieces on the black team
                        legal_moves = self.squaregrid[x][y].occupying_piece.legalMoves(self,self.squaregrid[x][y])

                        selected_square = self.squaregrid[x][y]
                        selected_piece = self.squaregrid[x][y].occupying_piece

                        #For all legal moves for a given piece, try the move and then check if there is still a check. If there is a still a check and move is illegal, loop through and see if any move is illegal=False (or to say, there is a legal move remaining)

                        for move in legal_moves:
                            #for each move, see if the result is not illegal. If we find a single move that blocks the check, no checkmate

                            backup_king_square = king_square
                            temp_square = self.squaregrid[move[0]][move[1]]
                            temp_square_piece = self.squaregrid[move[0]][move[1]].occupying_piece
                            back_current_piece = selected_piece

                            if selected_piece.color == 'w' and isinstance(selected_piece,King):
                                self.white_king_square = self.squaregrid[move[0]][move[1]]
                            elif selected_piece.color == 'b' and isinstance(selected_piece,King):
                                self.black_king_square = self.squaregrid[move[0]][move[1]]

                            #Move the piece and update the previous square to blank
                            self.squaregrid[move[0]][move[1]].occupying_piece = selected_square.occupying_piece
                            self.squaregrid[selected_square.row][selected_square.column].occupying_piece = ''

                            illegal = self.find_illegal_moves(temp_square.occupying_piece)

                            self.squaregrid[move[0]][move[1]].occupying_piece = temp_square_piece
                            self.squaregrid[selected_square.row][selected_square.column].occupying_piece = back_current_piece

                            if selected_square.occupying_piece.color == 'w' and isinstance(selected_square.occupying_piece,King):
                                self.white_king_square = backup_king_square
                            elif selected_square.occupying_piece.color == 'b' and isinstance(selected_square.occupying_piece,King):
                                self.black_king_square = backup_king_square

                            if not illegal:
                                checkmate = False
                                print('No Checkmate found yet')
                                break
        #Return True if there is no legal moves. It implies we never resulted with illegal = False above from any peice and any move
        return checkmate

    #Called after a piece as moved. If the piece is a Pawn and for its color hits the back rank, then convert into a queen. Takes the move square as an argument.
    def check_promotion(self,square):
        if isinstance(square.occupying_piece,Pawn) and square.occupying_piece.color == 'w' and square.row == 0:
            square.occupying_piece.kill()
            square.addPiece(self,'w','Q')

        elif isinstance(square.occupying_piece,Pawn) and square.occupying_piece.color == 'b' and square.row == 7:
            square.occupying_piece.kill()
            square.addPiece(self, 'b', 'Q')

    #Main logic for each click. This function does a couple of different things in squence. Takes a position as an arguement for where the user clicked
    # 1) If self.selected_peice is null, then this will count as the first click and select a piece.
    # 2) Second click, check if there is a selected piece and then continue with main logic
    def handle_click(self,pos):
        clicked_square = self.locate_square(pos)

        if (clicked_square.occupying_piece == '' and self.selected_piece is None):
            print("Not a selectable square")
            return

        #Cancel move if the player selects the same square twice.
        if self.selected_square == clicked_square:
            self.highlight_squares(self.selected_piece.legalMoves(self,self.selected_square))
            self.selected_piece = None
            self.selected_square = None
            return


        #Enter this loop when selecting a piece. Select the square and piece we want to target first.
        if self.selected_piece is None:
            if (clicked_square.occupying_piece != '' and clicked_square.occupying_piece.color == self.turn):
                self.selected_piece = clicked_square.occupying_piece
                self.selected_square = clicked_square

                legal_moves = self.find_legal_moves(self.selected_square)
                self.highlight_squares(legal_moves)

        else:

            #Grab the legal moves for the originally selected piece
            legal_moves = self.find_legal_moves(self.selected_square)
            self.highlight_squares(legal_moves)


            #If there is no moves, unselect the piece
            if len(legal_moves) == 0:
                self.selected_piece = None
                self.selected_square = None

            #Loop through each move for the piece. Check if the user selected a square that is in the move list to progress

            for move in legal_moves:
                if move[0] == clicked_square.row and move[1] == clicked_square.column:

                    if (clicked_square.occupying_piece != '' and self.selected_square != clicked_square):
                        clicked_square.occupying_piece.rect.center = (-100,-100)


                    #Backup pieces before the move

                    self.white_king_square.highlighted = False
                    self.black_king_square.highlighted = False
                    en_passant_square = None

                    if self.selected_square.occupying_piece.color == 'w' and isinstance(self.selected_square.occupying_piece,King):
                        self.white_king_square = clicked_square

                    elif self.selected_square.occupying_piece.color == 'b' and isinstance(self.selected_square.occupying_piece,King):
                        self.black_king_square = clicked_square

                    backup_piece = self.selected_square.occupying_piece
                    backup_square = self.selected_square
                    backup_clicked_square = clicked_square
                    backup_clicked_piece = clicked_square.occupying_piece

                    if isinstance(self.selected_square.occupying_piece,Pawn):
                        if (clicked_square.occupying_piece == '' and isinstance(self.squaregrid[clicked_square.row+1][clicked_square.column].occupying_piece,Pawn) and self.squaregrid[clicked_square.row+1][clicked_square.column].occupying_piece.color == 'b'):
                            en_passant_square = self.squaregrid[clicked_square.row+1][clicked_square.column]
                            print("EN PASSANT")
                        elif (clicked_square.occupying_piece == '' and isinstance(self.squaregrid[clicked_square.row-1][clicked_square.column].occupying_piece,Pawn) and self.squaregrid[clicked_square.row-1][clicked_square.column].occupying_piece.color == 'w'):
                            en_passant_square = self.squaregrid[clicked_square.row -1][clicked_square.column]
                            print("EN PASSANT")

                    # BEGIN MOVE:

                    clicked_square.occupying_piece = self.selected_piece
                    self.selected_piece.rect.center = (clicked_square.centerx, clicked_square.centery)
                    self.selected_square.occupying_piece = ''

                    #Now check if that move was illegal

                    illegal = self.find_illegal_moves(backup_piece)

                    # If the move is not valid, we will move the pieces back to where they were originally
                    if illegal:

                        en_passant_square = None
                        self.toggle_turn()
                        clicked_square.occupying_piece = backup_clicked_piece
                        if clicked_square.occupying_piece != '':
                            clicked_square.occupying_piece.rect.center = (backup_clicked_square.centerx, backup_clicked_square.centery)

                        self.selected_square.occupying_piece = backup_piece
                        if self.selected_square.occupying_piece != '':
                            self.selected_square.occupying_piece.rect.center = (backup_square.centerx, backup_square.centery)

                        #Revert global king position
                        if self.selected_square.occupying_piece.color == 'w' and isinstance(self.selected_square.occupying_piece, King):
                            self.white_king_square = backup_square

                        elif self.selected_square.color == 'b' and isinstance(self.selected_square.occupying_piece,King):
                            self.black_king_square = backup_square

                    #Continue if the move was valid
                    else:

                        self.selected_piece.move()
                        self.check_promotion(clicked_square)

                        if en_passant_square is not None:
                            en_passant_square.occupying_piece.rect.center = (-100, -100)
                            en_passant_square.occupying_piece = ''


                        #check for checkmate. Pass in the square location of where the last piece moved to. Return True/False
                        check_mate = self.is_checkmate(clicked_square)

                        if check_mate:
                            if self.turn == 'w':
                                highlight_list = [[self.black_king_square.row,self.black_king_square.column]]
                            else:
                                highlight_list = [[self.white_king_square.row, self.white_king_square.column]]

                            print("CHECK MATE!")

                    self.selected_piece = None
                    self.selected_square = None
                    self.toggle_turn()

    #Main game loop
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

            #This will mark the player grid of squares
            self.draw()

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()


#Here we start the game

game = Game()
game.new_game()