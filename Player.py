import pygame
try:
    import simplegui

except ImportError:

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Platform import *
class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.velocity = 0
        self.falling = True
        self.onGround = False

        self.image = pygame.image.load("character.png")
    def jump(self):
        if(self.onGround == True):
            self.velocity= 10
            self.onGround== False

    collision = False
    #Top collision
    #collision detection checks, this is comparing the corners of the player and the platform
    def detectCollisions(self, x1, y1, w1, h1, x2, y2, w2, h2):
        #This collision detection is kind of complex/I will try and find a simpler formula
        if (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):

            return True

        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):

            return True

        elif (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

            return True

        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

            return True

        else:

            return False



    def update(self, gravity, blocklist):

        if (self.velocity<0):
            self.falling=True

        PositionX, PositionY = 0, 0
        for Platform in blocklist:

            collision = self.detectCollisions(self.x,self.y,self.width,self.height,Platform.x,Platform.y,Platform.width,Platform.height)

            #if true is returned
            if (collision == True):
                PositionX = Platform.x
                PositionY = Platform.y
                break

        #this is what happens outside the for loops
        if(collision == True ):
            print("collsion")
            if (self.falling==True):
                self.falling = False
                self.onGround = True
                self.velocity = 0
                #minus the player height so that its on the top of the platform
                self.y = PositionY-self.height
        # if there is no collision the player will keeps falling
        else:
                print(" no Collision")
                self.velocity += gravity
                self.falling = True
                self.onGround = False

        self.y -= self.velocity
    def render(self, window):
        #pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, self.width, self.height))
        window.blit(self.image,(self.x,self.y,self.width,self.height))