'''Write a Python program to create a Game screen and add two rectangular sprites to it
using the Pygame library. Add controls to one of the sprites as well for up, down, left
and right movements.'''
import pygame
import random

pygame.init()

SPC = pygame.USEREVENT + 1
BGC = pygame.USEREVENT + 2

blue = pygame.Color('blue')
lightblue = pygame.Color('lightblue')
darkblue = pygame.Color('darkblue')

purple = pygame.Color('purple')
lightpurple = pygame.Color(200, 100, 200)
darkpurple = pygame.Color('indigo')
white = pygame.Color('white')


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPC))
            pygame.event.post(pygame.event.Event(BGC))
    def change_color(self):
        self.image.fill(random.choice([purple, lightpurple, darkpurple, white]))
def change_background_color():
    global bg_color
    bg_color = random.choice([blue, lightblue, darkblue])
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(white, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)
sp2 = Sprite(lightpurple, 20, 30)
sp2.rect.x = 250
sp2.rect.y = 200
sp2.velocity = [0, 0]
all_sprites_list.add(sp2)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")
bg_color = blue
screen.fill(bg_color)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == SPC:
            sp1.change_color()
        elif event.type == BGC:
            change_background_color()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        sp2.rect.y -= 2
    if keys[pygame.K_DOWN]:
        sp2.rect.y += 2
    if keys[pygame.K_LEFT]:
        sp2.rect.x -= 2
    if keys[pygame.K_RIGHT]:
        sp2.rect.x += 2
    
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()

         


         
