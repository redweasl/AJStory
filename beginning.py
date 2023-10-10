# Going to use pygame for 2D video game
import sys, pygame
pygame.init()

framerate = 30
size = width, height = pygame.display.get_desktop_sizes()[0][0] / 2, pygame.display.get_desktop_sizes()[0][1] / 2
speed = [2, 2]
black = 0, 0, 0
title = "AJStory"

print("Welcome to the AJStory project. Not much here yet, but I hope you enjoy! \n-Alex")

pygame.display.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode(size)
framedelay = int (1000 / framerate)

player = pygame.image.load("images/diger.png")
playerrect = player.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    playerrect = playerrect.move(speed)
    if playerrect.left < 0 or playerrect.right > width:
        speed[0] = -speed[0]
    if playerrect.top < 0 or playerrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(player, playerrect)
    pygame.display.flip()
    pygame.time.wait(framedelay)

