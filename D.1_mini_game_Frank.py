import pygame
import random
import os

# Initialisierung von Pygame
pygame.init()

# Spielfrequenz
snake_speed = 15

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)
orange = pygame.Color(255, 165, 0)

# Spielfeldgröße und Hintergrundbild
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
BACKGROUND_IMAGE = pygame.image.load("Z_BackSnake.jpg")  # Hintergrundbild laden
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
GAMEOVER_IMAGE = pygame.image.load("Z_background_pong.jpg")  # Game Over Bild laden
GAMEOVER_IMAGE = pygame.transform.scale(GAMEOVER_IMAGE, (WIDTH, HEIGHT))

# Fenster erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake Initialisierung
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_position = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction

# Score
score = 0

# Schriftart
font = pygame.font.Font(None, 36)

# Score-Anzeige Funktion
def draw_score():
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

# Game Over Funktion
def game_over():
    pygame.quit()  # Pygame beenden
    os.system("python F_End_Page.py")

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Snake Richtung aktualisieren
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Snake Bewegung
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake wächst, wenn es das Obst frisst
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    # Neues Obst spawnen
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
    fruit_spawn = True

    # Hintergrund anzeigen
    screen.blit(BACKGROUND_IMAGE, (0, 0))

    # Snake und Obst zeichnen
    for pos in snake_body:
        pygame.draw.rect(screen, blue, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, orange, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game Over Bedingungen
    if snake_position[0] < 0 or snake_position[0] > WIDTH-10 or snake_position[1] < 0 or snake_position[1] > HEIGHT-10:
        game_over()

    # Snake Körper berühren (Selbstkollision)
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Punktestand anzeigen
    draw_score()

    # Bildschirm aktualisieren
    pygame.display.update()

    # FPS einstellen
    clock.tick(snake_speed)
