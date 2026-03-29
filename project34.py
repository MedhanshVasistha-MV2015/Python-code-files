'''Write a Python program to create a Game screen and add two rectangular sprites to it
using the Pygame library. Add controls to one of the sprites as well for up, down, left
and right movements.'''
import pygame
import random
pygame.init()
SPC = pygame.USEREVENT + 1
BGC = pygame.USEREVENT + 2
blue = pygame.Color('Blue')
lightblue = pygame.Color('lightblue')
darkblue = pygame.Color('darkblue')
purple = pygame.Color('purple')
lightpurple = pygame.Color('lightpurple')
darkpurple = pygame.Color('darkpurple')
white = pygame.Color('white')
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1 , 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
                self.velocity[1] = -self.velocity[1]
                boundry_hit = True
        if boundry_hit:
             pygame.event.post(pygame.event.Event(SPC))
             pygame.event.post(pygame.event.Event(BGC))
    def change_color(self):
         self.image.fill(random.choice([purple,darkpurple,lightpurple]))
def change_bgcol():
    global bg_color
    bg_color = random.choice([blue,lightblue,darkblue])

all_sprites_list = pygame.sprite.Group()

         
