'''Write a Python program to add two sprites and create a custom event of changing the
colour of the sprites.'''
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
sprite1 = pygame.Surface((50, 50))
sprite1.fill((255, 0, 0))
sprite2 = pygame.Surface((50, 50))
sprite2.fill((0, 255, 0))
sprite1_rect = sprite1.get_rect()
sprite2_rect = sprite2.get_rect()
sprite1_rect.topleft = (50, 50)
sprite2_rect.topleft = (150, 50)
CCE = pygame.USEREVENT + 1
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == CCE:
            sprite1.fill((0, 0, 255))
            sprite2.fill((255, 255, 0))
    screen.fill((255, 255, 255))
    screen.blit(sprite1, sprite1_rect)
    screen.blit(sprite2, sprite2_rect)
    pygame.display.flip()
    pygame.time.delay(1000)
    pygame.event.post(pygame.event.Event(CCE))
pygame.quit()
