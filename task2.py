import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

rect = pygame.Rect(280, 180, 40, 40)
rect_color = RED

SPEED = 1

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
        rect.x += SPEED
    if keys[pygame.K_UP]:
        rect.y -= SPEED
    if keys[pygame.K_DOWN]:
        rect.y += SPEED
    
    if rect.left < 0:
        rect.left = 0
    if rect.right > 600:
        rect.right = 600
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > 400:
        rect.bottom = 400
    
    screen.fill(WHITE)
    
    pygame.draw.line(screen, (200, 200, 200), (300, 0), (300, 400), 1)
    pygame.draw.line(screen, (200, 200, 200), (0, 200), (600, 200), 1)
    
    pygame.draw.rect(screen, rect_color, rect)
    
    pygame.draw.rect(screen, BLUE, rect, 2)
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
sys.exit()
