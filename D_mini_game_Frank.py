import pygame
import random
import os
import sys

# Initialisierung von Pygame
pygame.init()

# Spielfrequenz
snake_speed = 30

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
orange = pygame.Color(255, 165, 0)

# Spielfeldgröße und Hintergrundbild
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
BACKGROUND_IMAGE = pygame.image.load("Z_BackSnake.jpg")  # Hintergrundbild laden
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

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
score_snake = 0

# Schriftart
font = pygame.font.Font(None, 36)

# Score-Anzeige Funktion
def draw_score():
    score_text = font.render(f"Score: {score_snake}", True, white)
    screen.blit(score_text, (10, 10))

# Game Over Funktion
def game_over():
    pygame.quit()  # Pygame beenden
    sys.exit()  # Das ganze Skript beenden

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
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
    if snake_position == fruit_position:
        score_snake += 10
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
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, orange, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game Over Bedingungen
    if snake_position[0] < 0 or snake_position[0] >= WIDTH or snake_position[1] < 0 or snake_position[1] >= HEIGHT:
        break

    # Snake Körper berühren (Selbstkollision)
    for block in snake_body[1:]:
        if snake_position == block:
            break

    # Punktestand anzeigen
    draw_score()

    # Bildschirm aktualisieren
    pygame.display.update()

    # FPS einstellen
    clock.tick(snake_speed)

# Pygame beenden
pygame.quit()

# Score in Umgebungsvariable speichern
os.environ["SCORE_SNAKE"] = str(score_snake)

# Externes Skript starten
next_file = "E_End_Page.py"
command = "python3" if sys.platform != "win32" else "python"
os.system(f"{command} {next_file} {score_snake}")

sys.exit()  # Sicherstellen, dass das Skript beendet wird

