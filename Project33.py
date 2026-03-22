'''Write a Python program to create a Pygame window. Add a rectangle and
text to the screen. Use the following parameters for creating this game
screen -
1. Window size (640, 480)
2. Set caption - My first game screen
3. Create a rectangle of the colour of your choice, positioned at the centre
of the screen
4. Display a text on the screen
5. The background colour of the screen - White (0, 0, 0)'''
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('My first game screen')
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))
    font = pygame.font.SysFont('timesnewroman', 30)
    text = font.render('this is a text', True, (0, 0, 0))
    pygame.draw.rect(screen,(random.randint(0,255), random.randint(0,255), random.randint(0,255)),pygame.Rect(270,190,100,100))
    screen.blit(text, (220, 150))
    pygame.display.flip()