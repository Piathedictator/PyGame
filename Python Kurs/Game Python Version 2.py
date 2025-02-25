import pygame
import random

# Initiale Spieleinstellungen
snake_speed = 10
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20

# Farben
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
orange = pygame.Color(255, 165, 0)

# Pygame initialisieren
pygame.init()

# Hintergrundbilder laden
BACKGROUND_IMAGE = pygame.image.load("Synthwave.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

GAME_OVER_IMAGE = pygame.image.load("game_over.jpg")  
GAME_OVER_IMAGE = pygame.transform.scale(GAME_OVER_IMAGE, (WIDTH, HEIGHT))

# Fenster erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Game Over Nachrichten
game_over_messages = [
    "Das ist ja nicht so gut gelaufen. Probier's nochmal!",
    "Anfängerfehler. Jetzt streng dich mal an!",
    "Hätte hätte Snake Game Kette. Da machste nix, probier's nochmal!"
]

def reset_game():
    """Setzt das Spiel zurück."""
    global snake_position, snake_body, fruit_position, direction, change_to, score
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, WIDTH // GRID_SIZE) * GRID_SIZE,
                      random.randrange(1, HEIGHT // GRID_SIZE) * GRID_SIZE]
    direction = 'RIGHT'
    change_to = direction
    score = 0

reset_game()  # Spielvariablen initialisieren

def show_score():
    """Zeigt den Score auf dem Bildschirm an."""
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

def game_over():
    """Zeigt den Game Over Bildschirm und wartet auf eine Eingabe."""
    screen.blit(GAME_OVER_IMAGE, (0, 0))
    message = random.choice(game_over_messages)
    
    lines = message.split(". ")  # Zeilenumbruch an Punkt und Leerzeichen
    y_offset = HEIGHT // 2 - (len(lines) * 20)  # Mittig ausrichten
    for line in lines:
        game_over_text = font.render(line, True, white)
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, y_offset))
        screen.blit(game_over_text, text_rect)
        y_offset += 40
    screen.blit(game_over_text, text_rect)

    # Restart-Button
    '''
    button_text = font.render("Restart", True, black)
    button_rect = pygame.Rect(50, 20, 100, 40)
    pygame.draw.rect(screen, white, button_rect)
    screen.blit(button_text, (WIDTH // 2 - 30, HEIGHT // 2 + 5))
    '''
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    reset_game()
                    return True

while True:
    # Events verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Richtung aktualisieren
    direction = change_to

    # Schlange bewegen
    if direction == 'UP':
        snake_position[1] -= GRID_SIZE
    elif direction == 'DOWN':
        snake_position[1] += GRID_SIZE
    elif direction == 'LEFT':
        snake_position[0] -= GRID_SIZE
    elif direction == 'RIGHT':
        snake_position[0] += GRID_SIZE

    # Schlange wächst, wenn sie das Obst frisst
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += 10
        fruit_position = [random.randrange(1, WIDTH // GRID_SIZE) * GRID_SIZE,
                          random.randrange(1, HEIGHT // GRID_SIZE) * GRID_SIZE]
    else:
        snake_body.pop()

    # Kollision mit den Wänden
    if snake_position[0] < 0 or snake_position[0] >= WIDTH or snake_position[1] < 0 or snake_position[1] >= HEIGHT:
        if not game_over():
            break

    # Kollision mit sich selbst
    if snake_position in snake_body[1:]:
        if not game_over():
            break

    # Hintergrund anzeigen
    screen.blit(BACKGROUND_IMAGE, (0, 0))

    # Schlange zeichnen (Kopf rot, Körper orange)
    for index, pos in enumerate(snake_body):
        color = red if index == 0 else orange
        pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE))

    # Obst zeichnen
    pygame.draw.rect(screen, white, pygame.Rect(fruit_position[0], fruit_position[1], GRID_SIZE, GRID_SIZE))

    # Score anzeigen
    show_score()

    # Bildschirm aktualisieren
    pygame.display.update()

    # Geschwindigkeit anpassen
    clock.tick(snake_speed)
