import os 
import sys
import pygame
from soldier import Soldier
from bullet import Bullet
from enemy import Enemy

pygame.init()
#Window settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The last stand")

#Fps
clock = pygame.time.Clock()

# Group of sprites
soldiers = pygame.sprite.Group()
soldier1 = Soldier(400, 540)
soldiers.add(soldier1)
selected_soldier = None
#Bullet group
bullets = pygame.sprite.Group()
test_bullet = Bullet((400,540),(1,0), 600)
bullets.add(test_bullet)
shoot_cooldown = 0.5
shoot_timer = 0
#Enemy Group
enemies = pygame.sprite.Group()
test_enemy = Enemy(1200, 540)
enemies.add(test_enemy)

# Main game loop
running = True
while running:
    dt = clock.tick(60) / 1000
    shoot_timer += dt
    if shoot_timer >=shoot_cooldown:
        bullet_x = soldier1.rect.centerx + 35
        bullet_y = soldier1.rect.centery + 5
        start_pos = pygame.Vector2(bullet_x, bullet_y)
        target_pos = pygame.Vector2(test_enemy.rect.center)
        direction = target_pos - start_pos
        direction = direction.normalize()
        new_bullet = Bullet(start_pos, direction, 600)
        bullets.add(new_bullet)
        shoot_timer = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            #Checking click on soldier
            if soldier1.rect.collidepoint(mouse_pos):
                soldier1.is_selected = True
                selected_soldier = soldier1
                # If the soldier is clicked, set the target position to the mouse position
            elif selected_soldier:
                selected_soldier.target_x = mouse_pos[0]
                selected_soldier.target_y = mouse_pos[1]
                selected_soldier.is_selected = False
                selected_soldier = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                test_enemy.set_state("attacking")
            elif event.key == pygame.K_3:
                test_enemy.set_state("death")
            elif event.key == pygame.K_1:
                test_enemy.set_state("walking")
                     

    
    enemies.update()            
    soldiers.update (dt)
    bullets.update(dt)
    screen.fill((30, 30, 30))
    enemies.draw(screen)
    soldiers.draw(screen)
    bullets.draw(screen)
    for soldier in soldiers:
        soldier.draw_selection(screen)
    pygame.display.flip()\

pygame.quit()
sys.exit()