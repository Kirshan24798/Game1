try:
    import simplegui

except ImportError:

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import pygame
from Player import *
from Platform import *
#Height and Width
HEIGHT = 800
WIDTH = 600
#initilise pygame
pygame.init()
#creating a window
window = pygame.display.set_mode((WIDTH,HEIGHT))
#caption
pygame.display.set_caption("Game Window")
gravity =-0.5
#color
black = (0,0,0)
Red = (50,0,0)

#defining the fps
clock = pygame.time.Clock()
player = Player(0,0)
#25 columns, 19 rows
#using a list to create the level, the grid (800/32) so working with 25 blocks and 19 blocks(rows)
Level = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1],

]
#the vlaue of the blocks is stored in this list
blocklist = []
#a for loop the range counts from 0-25, going through each coloumn
#the x goes through each zeros and if its one it will create a block.
#x32 because its 32 pixels
for y in range(0,len(Level)):
    for x in range(0,len(Level[y])):
        if(Level[y][x]==1):
            blocklist.append(platform(x*32,y*32))

#this is whats added to the players.x value
Xposition= 0
#loops as long as game loop is true
GameIsRunning = True
while GameIsRunning:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            GameIsRunning = False

        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
            player.x += -5
            print("left")
    if keys[pygame.K_RIGHT]:
            player.x += 5
            print("right")

    if keys[pygame.K_UP]:
            player.y += -7





    player.x += Xposition
    #simple background color
    window.fill(Red)
    #calling this will take the values from blocklist and create a rectangle in that position
    for platform in blocklist:
        platform.render(window)
    #movement using the Xposition vlaues

    #gravity so the player is always falling down
    player.update(gravity, blocklist,)
    #renders what is in the window,this case its the player rect with the position(x,y) and (W,H)

    player.render(window)
    #setting the fps
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
