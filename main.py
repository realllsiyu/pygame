import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Alice in Borderland')
clock = pygame.time.Clock()
title_font = pygame.font.Font('font/Pixeltype.ttf',50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surface = title_font.render('Alice in Borderland', False, 'Black')
score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):print('collide')
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(score_surface, score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface, player_rect)

    #if player_rect.colliderect(snail_rect):
    mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
    #    pygame.mouse

    pygame.display.update()
    clock.tick(60)