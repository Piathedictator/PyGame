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
TEXT_COLOR = black

# Initialisierung von Pygame
pygame.init()
pygame.font.init()

font = pygame.font.Font(None, 36)
size = 36

# Spielfeldgröße und Laden des Hintergrundbildes, Game_Over_screens
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
BACKGROUND_IMAGE = pygame.image.load("BackSnake.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
GAMEOVER_IMAGE = pygame.image.load("start_image.jpg")
GAMEOVER_IMAGE = pygame.transform.scale(GAMEOVER_IMAGE, (WIDTH, HEIGHT))

# Fenster erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# fruit position
fruit_position = [random.randrange(1, (WIDTH//10)) * 10, 
                  random.randrange(1, (HEIGHT//10)) * 10]
fruit_spawn = True

# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

def show_score():
    score_surface = font.render(f'Score: {score}', True, TEXT_COLOR)
    screen.blit(score_surface, (10, 10))

game_over_messages = [
    "Das ist ja nicht so gut gelaufen. Probier's nochmal!",
    "Anfängerfehler. Jetzt streng dich mal an!",
    "Hätte hätte Snake Game Kette. Da machste nix, probier's nochmal!",
    "Digga, dein Versagen kotzt mich an. Vallah!",
    "Du hast verloren. Geh nach Hause.",
    "Du hast schwach angefangen. Dann stark nachgelassen!",
    "Gamer? Eher Game Over!",
    "Schlangemörder!",
    "Digga, was war das?!",
    "Spielst du mit den Füßen oder wat?"
]

def game_over():
    screen.blit(GAMEOVER_IMAGE, (0, 0))
    message = random.choice(game_over_messages)
    lines = message.split(". ")
    y_offset = HEIGHT // 2 - (len(lines) * 20)
    for line in lines:
        game_over_text = font.render(line, True, TEXT_COLOR)
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, y_offset))
        screen.blit(game_over_text, text_rect)
        y_offset += 40
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    exit()

while True:
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
    
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += 10 
        fruit_spawn = False
    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WIDTH//10)) * 10, 
                          random.randrange(1, (HEIGHT//10)) * 10]
    fruit_spawn = True
    
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    for pos in snake_body:
        pygame.draw.rect(screen, blue, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    
    if snake_position[0] < 0 or snake_position[0] > WIDTH-10 or snake_position[1] < 0 or snake_position[1] > HEIGHT-10:
        game_over()
    
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    show_score()
    pygame.display.update()
    clock.tick(snake_speed)
