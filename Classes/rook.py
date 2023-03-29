from Classes.pieces import *

class Rook(Piece):

    def __init__(self, color, x, y, game):

        #we can call the parent class init to set our state
        super().__init__(color, x, y, game)

        self.image = pygame.image.load('Images/'+self.color+'R.svg')
        self.image = pygame.transform.scale(self.image, (240,240))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        print()
