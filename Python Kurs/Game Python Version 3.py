import pygame
import random

# Spielfeldparameter
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
snake_speed = 15

# Farben
green = pygame.Color(0, 255, 0)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

# Initialisierung von Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Hintergrundbild laden
BACKGROUND_IMAGE = pygame.image.load("Synthwave.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

# Schriftart
font = pygame.font.Font(None, 36)

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

def game_over():
    screen.fill(black)
    message = random.choice([
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
    ])
    game_over_text = font.render(message, True, white)
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    exit()

def main():
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE, 
                      random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE]
    direction = 'RIGHT'
    change_to = direction
    score = 0
    
    while True:
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
        
        direction = change_to
        if direction == 'UP':
            snake_position[1] -= GRID_SIZE
        elif direction == 'DOWN':
            snake_position[1] += GRID_SIZE
        elif direction == 'LEFT':
            snake_position[0] -= GRID_SIZE
        elif direction == 'RIGHT':
            snake_position[0] += GRID_SIZE
        
        snake_body.insert(0, list(snake_position))
        if snake_position == fruit_position:
            score += 10
            fruit_position = [random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE, 
                              random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE]
        else:
            snake_body.pop()
        
        # Kollisionsprüfung
        if (snake_position[0] < 0 or snake_position[0] >= WIDTH or
            snake_position[1] < 0 or snake_position[1] >= HEIGHT or
            snake_position in snake_body[1:]):
            game_over()
        
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, white, pygame.Rect(fruit_position[0], fruit_position[1], GRID_SIZE, GRID_SIZE))
        
        draw_score(score)
        pygame.display.update()
        clock.tick(snake_speed)

if __name__ == "__main__":
    main()