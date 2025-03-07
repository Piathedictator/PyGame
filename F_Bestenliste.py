import pygame
import os
import csv
import Y_config

player_name = str(os.getenv("PLAYER_NAME", "PLAYER"))
final_game_score = int(os.getenv("FINAL_GAME_SCORE", "0"))

# Initialize Pygame
pygame.init()

# Set up some constants
pygame.display.set_caption("Bestenliste")

screen = Y_config.SCREEN
background = pygame.image.load("Z_background.jpg")
background = pygame.transform.scale(background, (Y_config.WIDTH, Y_config.HEIGHT))

# Load the best player scores from the CSV file
best_player_scores = []
with open('player_scores.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        best_player_scores.append((row['Player'], int(row['Score'])))

# Sort the best player scores in descending order
best_player_scores.sort(key=lambda x: x[1], reverse=True)

# Create the "ENDE" button
ende_button = pygame.Rect(Y_config.WIDTH / 2 - 75, Y_config.HEIGHT - 100, 150, 50)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Beenden mit Taste "Q"
                pygame.quit()
                exit()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and ende_button.collidepoint(event.pos):
            running = False

    # Draw everything
    screen.blit(background, (0, 0))

    # Draw the final game score with shadow
    score_text = f"Dein Vergleich mit den Besten! {player_name}, {final_game_score}"
    score_lines = score_text.split("! ")
    score_y = 100
    for line in score_lines:
        # Add shadow
        score_part_shadow = Y_config.FONT_60.render(line, True, Y_config.BLACK)
        screen.blit(score_part_shadow, (Y_config.WIDTH / 2 - score_part_shadow.get_width() / 2 + 2, score_y + 2))
        
        # Main score text
        score_part = Y_config.FONT_60.render(line, True, Y_config.CYAN)
        screen.blit(score_part, (Y_config.WIDTH / 2 - score_part.get_width() / 2, score_y))
        score_y += 60

    # Draw the list of best players with a white background box
    best_player_y = 250
    box_width = Y_config.WIDTH - 300  # Set box width
    box_height = len(best_player_scores) * 40 + 20  # Adjust height based on the number of scores
    box_x = Y_config.WIDTH / 2 -150  # Box starting X position
    box_y = best_player_y - 10  # Box starting Y position
    
    pygame.draw.rect(screen, Y_config.WHITE, (box_x, box_y, box_width, box_height))  # White box behind the best player scores

    # Draw the best player scores
    for player, score in best_player_scores:
        player_text = Y_config.FONT_50.render(f"{player}: {score}", True, Y_config.BLACK)
        screen.blit(player_text, (200, best_player_y))
        best_player_y += 40

    # Draw the "ENDE" button
    pygame.draw.rect(screen, Y_config.WHITE, ende_button)
    ende_text = Y_config.FONT_50.render("ENDE", True, (0, 0, 0))
    screen.blit(ende_text, (Y_config.WIDTH / 2 - ende_text.get_width() / 2, Y_config.HEIGHT - 90))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
