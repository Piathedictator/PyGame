import pygame
import random
import sys
import os
import Y_config


pygame.init()

# Fenstergröße
width, height = Y_config.WIDTH, Y_config.HEIGHT
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong_Game")

# Hintergrundbild:
background = pygame.image.load("Z_pong.jpg")  # Bild laden
background = pygame.transform.scale(background, (width, height))  # Größe anpassen

# Variablen:
paddle_width, paddle_height = 15, 100
ball_size = 15
paddle_speed = 7
ball_speed_x, ball_speed_y = 5, -5  # Ball Geschwindigkeit
speed_multiplier = 1.03  # Erhöhung der Geschwindigkeit nach jedem Score

# Positioierung Objekte
player = pygame.Rect(height / 2, 570 , paddle_height, paddle_width)
ball = pygame.Rect(width / 2 , height / 2, ball_size, ball_size)

# Hindernisse random erstellen: 
obstacles = []
def create_obstacle():
    x = random.randint(100, width - 50)
    y = random.randint(200, height - 300)
    return pygame.Rect(x, y, 50, 20)

# Spielschleife
score_pong = 0
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background, (0, 0))

    # Beenden mit Taste "Q"
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  
                pygame.quit()
                exit()
        if event.type == pygame.QUIT:
            running = False

    # Steuerung für den Spieler (Pfeiltasten)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= paddle_speed
    if keys[pygame.K_RIGHT] and player.right < width:
        player.x += paddle_speed

    # Ballbewegung
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball-Kollision mit Wänden links & rechts
    if ball.left <= 0 or ball.right >= width:
        ball_speed_x *= -1

    # Ball-Kollision mit oberer Wand (Score) plus Geschwindigkeit steigern
    if ball.top <= 0:
        score_pong += 1
        ball_speed_x *= speed_multiplier  # Geschwindigkeit erhöhen x & y
        ball_speed_y *= -1 * speed_multiplier
        paddle_speed *= speed_multiplier

        if score_pong % 2 == 0:
            obstacles.append(create_obstacle())  # Alle 2 Scores wird Hinderniss erstellt
    
    # Ball-Kollision mit Hindernissen:
    for obstacle in obstacles[:]:
        if ball.colliderect(obstacle):
            ball_speed_y *= -1  
            obstacles.remove(obstacle) 

    # Ball-Kollision mit Spieler-Schläger
    if ball.colliderect(player):
        ball_speed_y *= -1   

    # Wenn der Ball unten verschwindet → Game Over
    if ball.bottom >= height:
        running = False

    # Schläger visualisieren:
    pygame.draw.rect(screen, Y_config.GRAY, (player.x + 2, player.y + 2, player.width, player.height))  # Schatten
    pygame.draw.rect(screen, Y_config.PURPLE, player)

    # Ball visualisieren:
    pygame.draw.ellipse(screen, Y_config.PINK, (ball.x + 2, ball.y + 2, ball.width, ball.height))  # Schatten
    pygame.draw.ellipse(screen, Y_config.PINK, ball) 

    # Hindernisse visualisieren
    obstacle_colour = (Y_config.PURPLE)
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_colour, obstacle)

    # Score anzeigen:
    score_text = Y_config.FONT_40.render(f"Score: {score_pong}", True, Y_config.BLACK)
    screen.blit(score_text, (width // 2 - 55, 20))

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()

# Nächste Seite öfnnen und Score übergeben
os.environ["SCORE_PONG"] = str(score_pong)
command = "python3" if sys.platform != "win32" else "python"
os.system(f"{command} C_First_Page_2048.py")