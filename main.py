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

        # This is the code as the entry point to start a new game.

    def newGame(self):

        self.all_sprites = pygame.sprite.LayeredUpdates()

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

        self.createBoard()
        self.createPieces()

        self.running()


    def createBoard(self):
        # Create all the square objects first
        blockSize = 90
        color = WHITE

        column = 0

        for x in range(0, WIDTH, blockSize):  # x coordinate
            color = self.flipColor(color)
            row = 0
            column = column + 1

            for y in range(0, HEIGHT, blockSize):  # y coordinate
                # Now we alternate the colours of the blocks
                color = self.flipColor(color)

                # Create the first square object in a 2d list
                # Also add in the occupying piece for the start

                self.squaregrid[column - 1].append(Square(x, y, color, blockSize, row, column - 1, ''))
                row = row + 1

    def createPieces(self):
        #Now we add each piece to the board squares.

        for x in range(8):
            for y in range(8):

                board_value = self.board[x][y]
                attributes = self.determinePiece(board_value)
                colour = attributes[0]
                piece_code = attributes[1]

                if piece_code != '--':
                    self.squaregrid[x][y].addPiece(self,colour,piece_code)

    def determinePiece(self,piece):
        #This function will return back what piece object based on the letters in the board array for setup

        values = piece.split()
        color = values[0][0]
        occupying_piece = values[0][1]

        if piece == '--':
            return ['--','--']
        else:

            return [color,occupying_piece]

    #Once we have the initial list of squares, now we can loop and draw them all
    def drawBoard(self):

        blockSize = 90 #Set the size of the grid block

        for x in range(8):
            for y in range(8):
                self.squaregrid[x][y].drawSquare(self.screen)

    def flipColor(self, color):
        WHITE = (240,240,240)
        BLACK = (30,30,30)
        if not color or color == WHITE:
            color = BLACK
        else:
            color = WHITE
        return color

    def draw(self):
        self.drawBoard()

        # Draw the pieces on the screen.
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


    def update(self):
        #self.all_sprites.update()
        return


    def running(self):

        # Set up the drawing window
        # We are going for W=1280, H=720
        screen = pygame.display.set_mode([HEIGHT, WIDTH])

        # Run until the user asks to quit
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("The user clicked the mouse")
                    print(pygame.mouse.get_pos())

                    #locate the selected sprite

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
game.newGame()