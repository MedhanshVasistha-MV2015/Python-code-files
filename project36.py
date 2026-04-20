'''Write a Python program to add one player and seven other enemy sprites (positioned
randomly) to the game screen. A variable score should have its values increased by
one whenever the sprites collide.'''
import pygame
import random
pygame.init()
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (500, 400))
screen = pygame.display.set_mode((500,400))
screen.blit(bg, (0, 0))
player = pygame.Surface((50, 50))
player.fill((0, 255, 0))
player_rect = player.get_rect()
player_rect.topleft = (50, 50)
enemies = []
for _ in range(7):
    enemy = pygame.Surface((50, 50))
    enemy.fill((255, 0, 0))
    enemy_rect = enemy.get_rect()
    enemy_rect.topleft = (random.randint(0, 450), random.randint(0, 350))
    enemies.append((enemy, enemy_rect))
score = 0
font = pygame.font.SysFont('freesansbold', 32)
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 2
    if keys[pygame.K_RIGHT]:
        player_rect.x += 2
    if keys[pygame.K_UP]:
        player_rect.y -= 2
    if keys[pygame.K_DOWN]:
        player_rect.y += 2
    for enemy, enemy_rect in enemies:
        enemy_rect.x += random.randint(-3, 3)
        enemy_rect.y += random.randint(-3, 3)
        if enemy_rect.left < 0:
            enemy_rect.left = 0
        if enemy_rect.right > 500:
            enemy_rect.right = 500
        if enemy_rect.top < 0:
            enemy_rect.top = 0
        if enemy_rect.bottom > 400:
            enemy_rect.bottom = 400
    for enemy, enemy_rect in enemies:
        if player_rect.colliderect(enemy_rect):
            score += 1
            enemy_rect.topleft = (random.randint(0, 450), random.randint(0, 350))
    screen.blit(player, player_rect)
    screen.blit(bg, (0, 0))
    screen.blit(player, player_rect)
    for enemy, enemy_rect in enemies:
        screen.blit(enemy, enemy_rect)
    score_text = font.render('Score: ' + str(score), True,(255, 255, 255))
    screen.blit(score_text, (10, 10))
    if score >= 10:
        win_text = font.render('You Win!', True, (255, 255, 0))
        screen.blit(win_text, (200, 200))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
