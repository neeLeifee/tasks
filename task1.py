import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

x_pos = 50
y_pos = 240
radius = 30
speed = 3

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    x_pos += speed

    if x_pos > 640 + radius:
        x_pos = -radius

    pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), radius)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
