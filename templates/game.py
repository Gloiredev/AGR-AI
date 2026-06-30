import pygame
import random
import os

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE SURVIVOR: BOSS EDITION")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)

# Couleurs
BLACK, CYAN, RED, WHITE, GOLD = (0,0,0), (0,255,255), (255,50,50), (255,255,255), (255,215,0)

# Système de Sauvegarde
def load_data():
    if os.path.exists("save.txt"):
        with open("save.txt", "r") as f:
            data = f.read().split(',')
            return int(data[0]), int(data[1]), int(data[2]) # score, level, high_score
    return 0, 1, 0

def save_data(s, l, hs):
    with open("save.txt", "w") as f:
        f.write(f("{s},{l},{hs}"))

# Variables de jeu
score, level, high_score = load_data()
health = 8
enemies = []
boss_active = False
boss_hp = 0
player_x = WIDTH // 2

def reset_game(full_reset=False):
    global health, enemies, boss_active, score, level
    health = 8
    enemies = []
    boss_active = False
    if full_reset:
        score, level = 0, 1

def draw_vaisseau(x, y):
    pts = [(x, y+30), (x+20, y), (x+40, y+30), (x+20, y+20)]
    pygame.draw.polygon(screen, CYAN, pts, 2)

def draw_meteor(x, y, size):
    pts = [(x+10, y), (x+size, y+10), (x+size-10, y+size), (x, y+size-5)]
    pygame.draw.polygon(screen, WHITE, pts, 1)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Boucle principale
run = True
while run:
    screen.fill(BLACK)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_data(score, level, high_score)
            run = False
        if event.type == pygame.KEYDOWN and health <= 0:
            if event.key == pygame.K_r: reset_game(True)

    if health > 0:
        # Contrôles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0: player_x -= 7
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 40: player_x += 7

        # Logique Boss
        if score > 0 and score % 50 == 0 and not boss_active:
            boss_active = True
            boss_hp = 10 + (level * 5)
            enemies = [] # On nettoie l'écran

        if not boss_active:
            # Apparition Météores
            if random.random() < 0.05 + (level * 0.01):
                enemies.append([random.randint(0, WIDTH-40), -40])
           
            for m in enemies[:]:
                m[1] += 5 + level
                if m[1] > HEIGHT:
                    enemies.remove(m)
                    score += 1
                # Collision
                if player_x < m[0]+30 and player_x+40 > m[0] and HEIGHT-60 < m[1]+30 and HEIGHT-20 > m[1]:
                    health -= 1
                    enemies.remove(m)
        else:
            # Comportement du Boss
            pygame.draw.rect(screen, GOLD, (WIDTH//2-100, 50, 200, 60), 3)
            draw_text(f"BOSS HP: {boss_hp}", font, GOLD, WIDTH//2-50, 70)
            # Le boss "descend" lentement pour mettre la pression
            if random.random() < 0.02: boss_hp -= 1 # Simulation de combat
            if boss_hp <= 0:
                boss_active = False
                level += 1
                score += 10 # Bonus
                save_data(score, level, high_score)

        # Dessins
        draw_vaisseau(player_x, HEIGHT-60)
        for m in enemies: draw_meteor(m[0], m[1], 30)

        # Interface
        pygame.draw.rect(screen, RED, (20, 20, health * 20, 15)) # Barre de vie
        draw_text(f"Score: {score}  Niv: {level}  Record: {high_score}", font, WHITE, 20, 45)

    else:
        draw_text("VAISSEAU DÉTRUIT", font, RED, WIDTH//2-100, HEIGHT//2)
        draw_text("Appuie sur R pour recommencer", font, WHITE, WIDTH//2-140, HEIGHT//2+40)
        if score > high_score: high_score = score

    pygame.display.flip()
    clock.tick(60)

pygame.quit()