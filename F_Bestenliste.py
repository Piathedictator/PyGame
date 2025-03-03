import pygame
import os
import csv
import sys
#from G_Game_Scores import save_game_score
#from B_First_Page_Pia import start_screen


player_name = str(os.getenv("PLAYER_NAME", "PLAYER"))
final_game_score = int(os.getenv("FINAL_GAME_SCORE", "0"))


# Initialize Pygame
pygame.init()

# Set up some constants
width, height = 600, 600
background_color = (0, 0, 0)
text_color = (255, 255, 255)
button_color = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bestenliste")

# Set up the font
font_title = pygame.font.Font(None, 50)
font = pygame.font.Font(None, 30)

# Load the best player scores from the CSV file
best_player_scores = []
with open('player_scores.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        best_player_scores.append((row['Player'], int(row['Score'])))

# Sort the best player scores in descending order
best_player_scores.sort(key=lambda x: x[1], reverse=True)

# Create the "ENDE" button
ende_button = pygame.Rect(width / 2 - 75, height - 100, 150, 50)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and ende_button.collidepoint(event.pos):
            running = False

    # Draw everything
    screen.fill(background_color)

    # Draw the final game score
    score_text = f"Endpunktestand:! {final_game_score}"
    score_lines = score_text.split("! ")
    score_y = 100
    for line in score_lines:
        score_part = font_title.render(line, True, text_color)
        screen.blit(score_part, (width / 2 - score_part.get_width() / 2, score_y))
        score_y += 60

    # Draw the list of best players
    best_player_y = 200
    for player, score in best_player_scores:
        player_text = font.render(f"{player}: {score}", True, text_color)
        screen.blit(player_text, (width / 2 - player_text.get_width() / 2, best_player_y))
        best_player_y += 40

    # Draw the "ENDE" button
    pygame.draw.rect(screen, button_color, ende_button)
    ende_text = font.render("ENDE", True, (0, 0, 0))
    screen.blit(ende_text, (width / 2 - ende_text.get_width() / 2, height - 90))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
