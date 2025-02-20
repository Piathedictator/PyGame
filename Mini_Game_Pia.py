import pygame

pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong_Game")

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Spiel-Variablen
paddle_width, paddle_height = 15, 100
ball_size = 15
paddle_speed = 7
ball_speed_x, ball_speed_y = 5, -5  # Ball startet nach oben
speed_multiplier = 1.005  # Erhöhung der Geschwindigkeit nach jedem Treffer

# Positionen
player = pygame.Rect(HEIGHT / 2, 570 , paddle_height, paddle_width)
ball = pygame.Rect(WIDTH / 2 , HEIGHT / 2, ball_size, ball_size)

# Punktestand
score = 0
font = pygame.font.Font(None, 40)

# Spielschleife
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Steuerung für den Spieler (Pfeiltasten)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.top > 0:
        player.x -= paddle_speed
    if keys[pygame.K_RIGHT] and player.bottom < HEIGHT:
        player.x += paddle_speed

    # Ballbewegung
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball-Kollision mit Wänden links & rechts
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1

    # Ball-Kollision mit oberer Wand (Punkt für Spieler)
    if ball.top <= 0:
        ball_speed_y *= -1
        score += 1  # Punkt hinzufügen

    # Ball-Kollision mit Spieler-Schläger
    if ball.colliderect(player):
        ball_speed_y *= -1  # Ball zurückschicken
        ball_speed_x *= speed_multiplier  # Geschwindigkeit erhöhen
        ball_speed_y *= speed_multiplier  # Geschwindigkeit erhöhen

    # Wenn der Ball links verschwindet → Game Over
    if ball.bottom >= HEIGHT:
        print(f"Game Over! Dein Score: {score}")
        running = False

    # Zeichnen
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Punktestand anzeigen
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 30, 20))

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
