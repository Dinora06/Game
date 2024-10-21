import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tank properties
tank_width = 40
tank_height = 20
tank_speed = 5

# Bullet properties
bullet_width = 5
bullet_height = 10
bullet_speed = 7

# Player tank
player_x = screen_width // 2
player_y = screen_height - tank_height - 10
player_speed = 0

# Enemy tanks
enemy_tanks = []
for i in range(5):
    enemy_x = random.randint(0, screen_width - tank_width)
    enemy_y = random.randint(50, 150)
    enemy_tanks.append([enemy_x, enemy_y])

# Bullets
bullets = []

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed = -tank_speed
            elif event.key == pygame.K_RIGHT:
                player_speed = tank_speed
            elif event.key == pygame.K_SPACE:
                # Fire a bullet
                bullet_x = player_x + tank_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed = 0
    
    # Move the player tank
    player_x += player_speed
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - tank_width:
        player_x = screen_width - tank_width
    
    # Draw the player tank
    pygame.draw.rect(screen, GREEN, (player_x, player_y, tank_width, tank_height))
    
    # Move and draw enemy tanks
    for enemy in enemy_tanks:
        enemy_x, enemy_y = enemy
        pygame.draw.rect(screen, RED, (enemy_x, enemy_y, tank_width, tank_height))
    
    # Move and draw bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
    
    for bullet in bullets:
        pygame.draw.rect(screen, BLUE, (bullet[0], bullet[1], bullet_width, bullet_height))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
