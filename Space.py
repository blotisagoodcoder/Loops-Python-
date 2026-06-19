import pygame
import random
import os
 

pygame.init()
pygame.mixer.init()
 
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader - Part 2")
clock = pygame.time.Clock()
 

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
 
background_img = pygame.image.load(os.path.join(ASSETS_DIR, "background.png"))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
 
shoot_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "shoot.wav"))
explosion_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "explosion.wav"))
 

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 

player_width, player_height = 50, 30
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 7
 

bullet_width, bullet_height = 5, 15
bullets = []
bullet_speed = 10
 

enemy_width, enemy_height = 40, 30
enemy_speed = 3
enemies = [[random.randint(0, WIDTH - enemy_width), random.randint(50, 200)] for _ in range(6)]
 
score = 0
font = pygame.font.SysFont("Arial", 24)
 

running = True
while running:
    clock.tick(60)
 
    
    screen.blit(background_img, (0, 0))
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])
                shoot_sound.play()
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
 
    
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
 
    
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemy[0] = random.randint(0, WIDTH - enemy_width)
            enemy[1] = 0
 
    
    for bullet in bullets[:]:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
            if bullet_rect.colliderect(enemy_rect):
                explosion_sound.play()
                if bullet in bullets:
                    bullets.remove(bullet)
                enemy[0] = random.randint(0, WIDTH - enemy_width)
                enemy[1] = 0
                score += 10
                break
 
    
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
 
    
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))
 
    
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))
 
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
 
    pygame.display.flip()
 
pygame.quit()