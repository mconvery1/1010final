import pygame
import random
import time

pygame.init()

display_width, display_height = 800, 600
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic or drawing here

    pygame.display.update()
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()
