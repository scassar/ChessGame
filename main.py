# Simple pygame program

# Import and initialize the pygame library
import pygame
from settings import *
from Sprites.pieces import *

#Manage the overall game state. IF we dont use this we have to define everything as global which isnt as nice.

class PiecesList(Enum):
    BPAWN = "bP.svg"
    BKNIGHT = "bN.svg"
    BROOK = "bR.svg"
    BBISHOP = "bB.svg"
    BQUEEN = "bQ.svg"
    BKING = "bK.svg"
    WPAWN = "wP.svg"
    WKNIGHT = "wN.svg"
    WROOK = "wR.svg"
    WBISHOP = "wB.svg"
    WQUEEN = "wQ.svg"
    WKING = "wK.svg"

class Game():

    def __init__(self):
        # initialise the module
        pygame.init()
        pygame.display.set_caption(GAMENAME)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))

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


    def drawBoard(self):

        blockSize = 90 #Set the size of the grid block
        color = WHITE

        for x in range(0, WIDTH, blockSize):
            color = self.flipColor(color)

            #Draw the colour square

            for y in range(0, HEIGHT, blockSize):
                #Now we alternate the colours of the blocks
                    color = self.flipColor(color)

                    rect = pygame.Rect(x, y, x+blockSize, y+blockSize)
                    #Set the last param of 0 to 1 if you want it to be lines only.
                    pygame.draw.rect(self.screen, color, rect, 0)



    #Code to setup all the pieces for the board
    def newGame(self):

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.bpawns = []
        self.wpawns = []
        self.whitepieces = []
        self.blackpieces = []

        #representation of the current board
        self.board = [
			['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
			['b ', 'b ', 'b ', 'b ', 'b ', 'b ', 'b ', 'b '],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['w ', 'w ', 'w ', 'w ', 'w ', 'w ', 'w ', 'w '],
			['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
		]




        #set up all pieces
        #we need an array that has a piece type, and a tile

        #White row

        self.whitepieces.append(Piece(WHITE, 60, 60,1,PiecesList.WROOK,self))
        self.whitepieces.append(Piece(WHITE, 60, 60,8,PiecesList.WROOK,self))
        self.whitepieces.append(Piece(WHITE, 60, 60,2,PiecesList.WKNIGHT,self))
        self.whitepieces.append(Piece(WHITE, 60, 60,7,PiecesList.WKNIGHT,self))
        self.whitepieces.append(Piece(WHITE, 60, 60,3,PiecesList.WBISHOP,self))
        self.whitepieces.append(Piece(WHITE, 60, 60,6,PiecesList.WBISHOP,self))
        self.whitepieces.append(Piece(WHITE, 60, 60, 5, PiecesList.WQUEEN, self))
        self.whitepieces.append(Piece(WHITE, 60, 60, 4, PiecesList.WKING, self))

        #Black row
        self.blackpieces.append(Piece(BLACK, 60, 60,64,PiecesList.BROOK,self))
        self.blackpieces.append(Piece(BLACK, 60, 60,57,PiecesList.BROOK,self))
        self.blackpieces.append(Piece(BLACK, 60, 60,63,PiecesList.BKNIGHT,self))
        self.blackpieces.append(Piece(BLACK, 60, 60,58,PiecesList.BKNIGHT,self))
        self.blackpieces.append(Piece(BLACK, 60, 60,62,PiecesList.BBISHOP,self))
        self.blackpieces.append(Piece(BLACK, 60, 60,59,PiecesList.BBISHOP,self))
        self.blackpieces.append(Piece(BLACK, 60, 60, 61, PiecesList.BQUEEN, self))
        self.blackpieces.append(Piece(BLACK, 60, 60, 60, PiecesList.BKING, self))

        #8 list of black pawns
        for i in range(8):
            self.wpawns.append(Piece(WHITE, 60, 60, 16-i, PiecesList.WPAWN, self))
        #8 White pawns
        for i in range(8):
            self.bpawns.append(Piece(BLACK, 60, 60, 56-i, PiecesList.BPAWN, self))

        self.running()

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