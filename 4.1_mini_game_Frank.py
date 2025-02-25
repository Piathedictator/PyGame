# importing libraries
import pygame
import time
import random

snake_speed = 15

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
orange = pygame.Color(255, 165, 0)
TEXT_COLOR = black

# Initialisierung von Pygame

pygame.init()
pygame.font.init()

font = pygame.font.Font(None, 36)
size = 36

# Spielfeldgröße und Laden des Hintergrundbildes, Game_Over_screens
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
BACKGROUND_IMAGE = pygame.image.load("BackSnake.jpg")  # Hintergrundbild laden
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
GAMEOVER_IMAGE = pygame.image.load("background_pong.jpg")  # Game Over Bild laden
GAMEOVER_IMAGE = pygame.transform.scale(GAMEOVER_IMAGE, (WIDTH, HEIGHT))


# Fenster erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (WIDTH//10)) * 10, 
                  random.randrange(1, (HEIGHT//10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(None, 36)
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    # displaying text
    screen.blit(score_surface, score_rect)
   
# Schriftart für Score-Anzeige
font = pygame.font.Font(None, 36)

# Game Over Nachrichten
game_over_messages = [
    "Das ist ja nicht so gut gelaufen.: Probier's nochmal!",
    "Anfängerfehler.: Jetzt streng dich mal an!",
    "Hätte hätte Snake Game Kette.: Da machste nix, probier's nochmal!",
    "Digga, dein Versagen kotzt mich an.: Vallah!",
    "Du hast verloren.: Geh nach Hause.",
    "Du hast schwach angefangen.: Dann stark nachgelassen!",
    "Gamer?: Eher Game Over!",
    "Loooooooser!!!",
    "Digga, was war das?!",
    "Spielst du mit den Füßen oder wat?",
    "Liegt dein Versagen am Spiel?: Ich denke nicht."
]

def draw_score():
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

def game_over():
    screen.blit(GAMEOVER_IMAGE, (0, 0))  # Game Over Hintergrundbild einblenden
    message = random.choice(game_over_messages)
    lines = message.split(": ")  # Zeilenumbruch an Punkt und Leerzeichen
    y_offset = HEIGHT // 2 - (len(lines) * 20)  # Mittig ausrichten
    for line in lines:
        game_over_text = font.render(line, True, TEXT_COLOR)
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, y_offset))
        screen.blit(game_over_text, text_rect)
        y_offset += 40
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return True


# Main Function
while True:
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two 
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Wachstumsmechanismus der Schlange
    # Wenn Früchte und Schlange kolldieren, dann score
    # Erhöhung des Scores um 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10 
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WIDTH//10)) * 10, 
                          random.randrange(1, (HEIGHT//10)) * 10]
        
    fruit_spawn = True

    # Hintergrundbild anzeigen
    screen.blit(BACKGROUND_IMAGE, (0, 0))

    # Die Schlange und das Obst zeichnen
    for pos in snake_body:
        pygame.draw.rect(screen, blue,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    #Obst Farbe und Größe einstellen
    pygame.draw.rect(screen, orange, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > WIDTH-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > HEIGHT-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
