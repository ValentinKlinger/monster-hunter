import pygame
pygame.init()

# class of the player

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 3
        self.weapon = None
        self.velocity = 5
        self.jump = 5
        self.image = pygame.image.load('assets/balle.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 500

# create the game windows

pygame.display.set_caption("The Ball Odyssey")
windows = pygame.display.set_mode((1040, 720))
windows.fill((96, 96, 96))


# import the player

player = Player()
player.image = pygame.transform.scale(player.image, (70, 70))

running = True

# while of the game
while running:

    windows.blit(player.image, player.rect)
    pygame.display.flip()

    # if the player close the windows

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
