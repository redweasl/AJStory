# Going to use pygame for 2D video game
import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("images/ball.png")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

