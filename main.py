import pygame
pygame.init()

# create the game windows

pygame.display.set_caption("The Ball Odyssey")
windows = pygame.display.set_mode((1080, 720))
windows.fill((96, 96, 96)) 
pygame.display.flip()

running = True

# while of the game
while running:

    # if the player close the windows

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
