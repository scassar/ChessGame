# Simple pygame program

# Import and initialize the pygame library
from Classes.square import *

#Manage the overall game state. IF we dont use this we have to define everything as global which isnt as nice.

class Game():

    def __init__(self):
        # initialise the module
        pygame.init()
        pygame.display.set_caption(GAMENAME)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.selected_piece = None
        self.selected_square = None


        # This is the code as the entry point to start a new game.

    def new_game(self):

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


    def handle_click(self,pos):
        clicked_square = self.locate_square(pos)

        if (clicked_square.occupying_piece == '' and self.selected_piece is None):
            print("Not a selectable square")
            return

        #For later, the move function should be attached to a piece object.

        #Enter this loop when selecting a piece. Select the square and piece we want to target first.
        if self.selected_piece is None:
            if (clicked_square.occupying_piece != '' and clicked_square.occupying_piece.color == self.turn):
                self.selected_piece = clicked_square.occupying_piece
                self.selected_square = clicked_square

                highlight_moves = self.find_legal_moves(self.selected_square, clicked_square)
                #update all squares in highlight_moves array

                self.highlight_squares(highlight_moves)

        else:

            #Legal moves will return the row/column that our selected piece can move to as a piece with logic

            legal_moves = self.find_legal_moves(self.selected_square, clicked_square)
            highlight_moves = legal_moves

            if len(legal_moves) == 0:
                self.selected_piece = None
                self.selected_square = None

            #Check if the square is available for clicking
            #print(self.selected_piece)
            for square_options in legal_moves:
                if square_options[0] == clicked_square.row and square_options[1] == clicked_square.column:

                    if (clicked_square.occupying_piece != '' and self.selected_square != clicked_square):
                        clicked_square.occupying_piece.rect.center = (-100,-100)
                        print("removing object and moving it off the board")

                #Check for legal move. What we need to know here is the from square, peice and target square

                #Set the new square = to the selected square and update the piece.

                    clicked_square.occupying_piece = self.selected_piece
                    self.selected_piece.rect.center = (clicked_square.centerx, clicked_square.centery)
                    self.selected_square.occupying_piece = ''

                    #No more piece is selected
                    self.selected_piece = None
                    self.selected_square = None
                    self.toggle_turn()
                    self.highlight_squares(highlight_moves)


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