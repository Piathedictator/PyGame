import pygame
import sys
import os

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
input_box = pygame.Rect(width / 2 - 100, height / 2 - 50, 200, 40)

# Buttons
start_button = pygame.Rect(width / 2 - 75, height / 2 + 50, 150, 50)
ok_button = pygame.Rect(width / 2 - 50, height / 2 + 120, 100, 40)

# Funktion zum Zeichnen der Startseite
def name_input_screen():
    global player_name
    running = True
    while running:
        screen.blit(background, (0, 0))
        
        # Anweisungen
        instruction_text = font_instruction.render("Gib deinen Spielernamen ein:", True, pink)
        screen.blit(instruction_text, (width / 2 - instruction_text.get_width() / 2, 200))
        
        # Eingabefeld für Namen
        pygame.draw.rect(screen, white, input_box)
        name_text = font.render(player_name, True, black)
        screen.blit(name_text, (input_box.x + 10, input_box.y + 5))
        
        # OK Button
        pygame.draw.rect(screen, white, ok_button)
        ok_text = font.render("OK", True, black)
        screen.blit(ok_text, (ok_button.x + 10, ok_button.y + 5))
        
        # Start Button
        pygame.draw.rect(screen, white, start_button)
        start_text = font.render("Start Spiel", True, black)
        screen.blit(start_text, (start_button.x + 10, start_button.y + 10))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Eingabefeld für Namen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode
            
            # OK Button
            if event.type == pygame.MOUSEBUTTONDOWN and ok_button.collidepoint(event.pos):
                print(f"Spielername: {player_name}")  # Optional: Hier könnte der Name gespeichert oder weitergegeben werden
            
            # Start Button
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                # Startet das erste Spiel
                print("Spiel wird gestartet!")
                os.system("python First_Page_Pia.py")
                running = False

# Aufruf der Seite für die Namensabfrage
name_input_screen()