'''Write a Python program to create a Pygame window. Add an image to the
screen, positioned at the centre. Use the following parameters for creating
this game screen -
1. Window size (500, 500)
2. Set caption - My first game screen
3. Image size (300, 300), positioned at the centre of the screen
4. The background colour of the screen - Grey (58, 58, 58)'''
import pygame
pygame.init()
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('My first game screen')
image = pygame.image.load('271333.jpg')
image = pygame.transform.scale(image, (300, 300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    screen.fill((58, 58, 58))
    image1 = image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
    screen.blit(image, image1)
    pygame.display.flip()
