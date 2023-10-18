import sys, pygame, math

class Player:
    def __init__(self):
        self.speed = 2
        self.sprite = pygame.image.load("images/Diger.png")
        self.hitbox = self.sprite.get_rect()
        self.position = pygame.math.Vector2(0, 0)
        self.move = pygame.math.Vector2(0, 0)
        self.destination = ()
    
    def movePlayer(self, dt):
        # Check for player input

        #WASD/arrows: Player moves
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.destination = ()
            self.move.y -= self.speed * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.destination = ()
            self.move.y += self.speed * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.destination = ()
            self.move.x -= self.speed * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.destination = ()
            self.move.x += self.speed * dt
        
        # Diagonal movement needs magnitude to be the same: do this by multiplying by sqrt(0.5)
        # The formula: 1 = 2x**2, x**2 = 0.5, x = sqrt(0.5)
        if self.move[0] != 0.0 and self.move[1] != 0.0:
            self.move.x *= math.sqrt(0.5)
            self.move.y *= math.sqrt(0.5)
        
        # If the player has a destination to go to, move towards that destination
        if self.destination != ():
            self.position = self.position.move_towards(self.destination, self.speed * dt)

        self.position += self.move
        self.move.x = 0
        self.move.y = 0
        self.hitbox.center = self.position
    
    def setDestination(self, pos):
        self.destination = pos

def main():
    # Pygame setup
    pygame.init()
    size = width, height = pygame.display.get_desktop_sizes()[0][0] / 2, pygame.display.get_desktop_sizes()[0][1] / 2
    title = "AJStory"

    pygame.display.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player = Player()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.setDestination(pygame.mouse.get_pos())

        # Player movement
        player.movePlayer(dt)

        # Screen fills with a color
        screen.fill("green")

        # Game renders here
        screen.blit(player.sprite, player.hitbox)

        # flip() the display to update the screen
        pygame.display.flip()

        dt = clock.tick(60) / 4 # limits FPS to 60
    pygame.quit()


main()