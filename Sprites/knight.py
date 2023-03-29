from Sprites.pieces import *

class Knight(Piece):

    def __init__(self, color, x, y, game):

        self.groups = game.all_sprites
        self.layers = 1
        self.game = game
        self.color = color
        self.x = x
        self.y = y

        #add sprite to the game all_sprites group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load('Images/'+self.color+'N.svg')
        self.image = pygame.transform.scale(self.image, (240,240))

        #Determine the position now
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

