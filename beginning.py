# Going to use pygame for 2D video game
import sys, pygame
pygame.init()

size = width, height = pygame.display.get_desktop_sizes()[0][0] / 2, pygame.display.get_desktop_sizes()[0][1] / 2
speed = [2, 2]
black = 0, 0, 0
title = "AJStory"

print("Welcome to the AJStory project. Not much here yet, but I hope you enjoy! \n-Alex")

pygame.display.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode(size)
runtime = pygame.time.Clock()

# Debug text, for now it'll only show fps
debugger = pygame.font.Font(None, 20)

player = pygame.image.load("images/diger.png")
playerrect = player.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    playerrect = playerrect.move(speed) # Move around the screen
    if playerrect.left < 0 or playerrect.right > width:
        speed[0] = -speed[0]
    if playerrect.top < 0 or playerrect.bottom > height:
        speed[1] = -speed[1]

    # Update the debugger fps
    debugtext = "fps: " + str(runtime.get_fps())
    debugsurface = debugger.render(debugtext, False, (255, 255, 255))
    debugrect = debugsurface.get_rect()

    screen.fill(black)
    screen.blit(player, playerrect)
    screen.blit(debugsurface, debugrect)
    pygame.display.flip()
    runtime.tick(30) # Run at 30 frames a second
