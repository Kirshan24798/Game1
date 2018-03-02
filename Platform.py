import pygame
try:
    import simplegui

except ImportError:

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class platform:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
        self.width= 32
        self.height =5




    def render (self, window):
        simplegui.draw.rect(window,(225,225,225),(self.x,self.y, self.width, self.height))