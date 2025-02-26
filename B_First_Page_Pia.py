import pygame
import sys
import os

pygame.init()

# Fenstergröße
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong - Startseite")

# Player Name aus Skript übernehmen
player_name = sys.argv[1] if len(sys.argv) > 1 else "Player"

background = pygame.image.load("Z_background_pong.jpg")  # Bild laden
background = pygame.transform.scale(background, (width, height))  # Größe anpassen

# Farben
white = (255, 255, 255)
blue = (173, 216, 230)
gray = (180, 180, 180)

# Schriftart
font = pygame.font.Font(None, 50)
font_instruction = pygame.font.Font(None, 40)
info_font = pygame.font.Font(None, 30)

# Info-Symbol
info_button = pygame.Rect(width / 2 - 15, height / 2 + 75, 30, 30)

def start_screen(info_text, next_file):
    info_visible = False
    start_button = pygame.Rect(width / 2 - 75, height / 2, 150, 50)
    running = True
    
    while running:
        screen.blit(background, (0, 0))
        
        # Titel:
        title_text = font.render(f"Hallo {player_name}!", True, white)
        screen.blit(title_text, (width / 2 - title_text.get_width() / 2, 150))

        # Instruction Text:
        instructions_text = font_instruction.render("Das erste Spiel ist Pong", True, white)
        screen.blit(instructions_text, (width / 2 - instructions_text.get_width() / 2, 200))
        
        # Start Button
        pygame.draw.rect(screen, white, start_button)
        button_text = font.render("Start", True, (0, 0, 0))
        screen.blit(button_text, (width / 2 - button_text.get_width() / 2, height / 2 + 10))
        
        # Info-Symbol
        pygame.draw.circle(screen, blue, info_button.center, 15)
        info_icon = font.render("i", True, white)
        screen.blit(info_icon, (info_button.x + 10, info_button.y))
        
        # Info-Text anzeigen, wenn aktiv
        if info_visible:
            for i, line in enumerate(info_text):
                text_surface = info_font.render(line, True, white)
                screen.blit(text_surface, (width / 2 - 200, (height / 2 + 120) + i * 20))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                running = False
            if event.type == pygame.MOUSEMOTION:
                info_visible = info_button.collidepoint(event.pos)

    command = "python3" if sys.platform != "win32" else "python"
    os.system(f"{command} {next_file}")

# **Kein automatischer Aufruf mehr!**  
if __name__ == "__main__":
    default_info_text = [
        "Steuere den Schläger mit den Pfeiltasten.",
        "Halte den Ball im Spiel und sammle Punkte.",
        "Drücke den Start-Button, um zu beginnen.",
    ]
    start_screen(default_info_text, "B.1_Mini_Game_Pia.py")
