import pygame
import sys
import os
import json

pygame.init()

# Fenstergröße
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spielseite")

background = pygame.image.load("start_image.jpg")  # Bild laden
background = pygame.transform.scale(background, (width, height))  # Größe anpassen

# Farben
white = (255, 255, 255)
pink = (251, 0, 255)
black = (0, 0, 0)

# Schriftarten
font = pygame.font.Font(None, 50)
font_title = pygame.font.Font(None, 70)
font_instruction = pygame.font.Font(None, 30)

# Eingabefelder
player_name = ""
input_box = pygame.Rect(width / 2 - 100, 100, 200, 40)

# Buttons
start_button = pygame.Rect(width / 2 - 75, 500, 150, 50)

# Score Liste
score = 0
high_scores = []

# Funktion zum Zeichnen der Seite mit Namensabfrage und High Scores
def name_input_and_high_scores_screen():
    global player_name, score, high_scores
    running = True
    while running:
        screen.blit(background, (0, 0))
        
        # Anweisungen und Namensfeld
        instruction_text = font_instruction.render("Gib deinen Spielernamen ein:", True, pink)
        screen.blit(instruction_text, (width / 2 - instruction_text.get_width() / 2, 60))
        
        pygame.draw.rect(screen, white, input_box)
        name_text = font.render(player_name, True, black)
        screen.blit(name_text, (input_box.x + 10, input_box.y + 5))
        
        # Start Button
        pygame.draw.rect(screen, white, start_button)
        start_text = font.render("Start Spiel", True, black)
        screen.blit(start_text, (start_button.x + 10, start_button.y + 10))
        
        # Anzeige der High Scores
        title_text = font_title.render("Top 5 Scores", True, pink)
        screen.blit(title_text, (width / 2 - title_text.get_width() / 2, 200))
        
        for i, score_entry in enumerate(high_scores):
            score_text = font.render(f"{i+1}. {score_entry['name']} - {score_entry['score']}", True, pink)
            screen.blit(score_text, (width / 2 - score_text.get_width() / 2, 250 + i * 40))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Eingabefeld für Namen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == pygame.K_RETURN:
                    print(f"Spielername: {player_name}")  # Hier kannst du den Namen weiterverwenden
                else:
                    player_name += event.unicode
            
            # Start Button
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                # Starte das Spiel
                print("Spiel wird gestartet!")
                os.system("python 2_First_Page_Pia.py")
                
                # Hier kannst du den Score speichern (z.B. score = 100)
                score = 0  # Zum Beispiel
                # Speichere den Spielernamen und Score
                high_scores.append({"name": player_name, "score": score})
                high_scores.sort(key=lambda x: x['score'], reverse=True)  # Sortiere absteigend nach Score
                high_scores = high_scores[:5]  # Top 5 Scores behalten
                
                # Speichere die Scores in einer Datei
                with open("high_scores.json", "w") as f:
                    json.dump(high_scores, f)
                
                running = False

# Lädt die gespeicherten High Scores, falls die Datei existiert
try:
    with open("high_scores.json", "r") as f:
        high_scores = json.load(f)
except FileNotFoundError:
    high_scores = []

# Aufruf der Seite für die Namensabfrage und Anzeige der High Scores
name_input_and_high_scores_screen()