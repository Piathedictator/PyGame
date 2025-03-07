import pygame
import sys
import os
import Y_config

pygame.init()

# Fenstergröße setzen
width, height = Y_config.WIDTH, Y_config.HEIGHT
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong - Startseite")

# Spielername aus Umgebungsvariablen übernehmen (Standard: "Player")
player_name = os.getenv("PLAYER_NAME", "Player")

# Hintergrundbild laden und auf Fenstergröße skalieren
background = pygame.image.load("Z_background.jpg")
background = pygame.transform.scale(background, (width, height))

# Info-Button als Kreis (Symbol für Informationen)
info_button = pygame.Rect(width / 2 - 15, height / 2 + 75, 30, 30)

# Funktion zum Anzeigen des Startbildschirms
def start_screen(title_text, instructions_text, info_text, next_file):
    info_visible = False  # Steuert, ob die Info-Box angezeigt wird
    start_button = pygame.Rect(width / 2 - 75, height / 2, 150, 50)  # Start-Button
    info_box = pygame.Rect(width / 2 - 240, height / 2 + 110, 480, 80)  # Box für Info-Text

    running = True
    while running:
        screen.blit(background, (0, 0))  # Hintergrund zeichnen
        
        # Titel mit Schatteneffekt rendern
        shadow_offset = 2
        title_shadow = Y_config.FONT_60.render(title_text.format(player_name=player_name), True, Y_config.BLACK)
        screen.blit(title_shadow, (width / 2 - title_shadow.get_width() / 2 + shadow_offset, 150 + shadow_offset))
        title_surface = Y_config.FONT_60.render(title_text.format(player_name=player_name), True, Y_config.CYAN)
        screen.blit(title_surface, (width / 2 - title_surface.get_width() / 2, 150))

        # Spielanleitung mit Schatteneffekt rendern
        instructions_shadow = Y_config.FONT_50.render(instructions_text, True, Y_config.BLACK)
        screen.blit(instructions_shadow, (width / 2 - instructions_shadow.get_width() / 2 + shadow_offset, 200 + shadow_offset))
        instructions_surface = Y_config.FONT_50.render(instructions_text, True, Y_config.CYAN)
        screen.blit(instructions_surface, (width / 2 - instructions_surface.get_width() / 2, 200))
        
        # Hinweis zum Beenden des Spiels
        exit_text = Y_config.FONT_30.render("Drück Q um das Spiel zu beenden", True, Y_config.CYAN) 
        screen.blit(exit_text, ((30, 570)))

        # Start-Button zeichnen
        pygame.draw.rect(screen, Y_config.WHITE, start_button)
        button_text = Y_config.FONT_60.render("Start", True, Y_config.BLACK)
        screen.blit(button_text, (width / 2 - button_text.get_width() / 2, height / 2 + 5))
        
        # Info-Button als Kreis mit "i"-Symbol
        pygame.draw.circle(screen, Y_config.BLACK, info_button.center, 15)
        info_icon = Y_config.FONT_50.render("i", True, Y_config.WHITE)
        screen.blit(info_icon, (info_button.x + 10, info_button.y))
        
        # Info-Box mit Erklärungen anzeigen, falls aktiv
        if info_visible:
            pygame.draw.rect(screen, Y_config.WHITE, info_box)  # Box zeichnen
            for i, line in enumerate(info_text):  # Mehrzeiligen Info-Text anzeigen
                text_surface = Y_config.FONT_30.render(line, True, Y_config.BLACK)
                screen.blit(text_surface, (width / 2 - text_surface.get_width()/2, (height / 2 + 120) + i * 20))
        
        pygame.display.flip()  # Bildschirm aktualisieren
        
        # Ereignisse (Events) verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Beenden des Spiels mit "Q"
                    pygame.quit()
                    exit()
            if event.type == pygame.QUIT:  # Fenster schließen
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):  # Klick auf den Start-Button
                    running = False
            if event.type == pygame.MOUSEMOTION:
                info_visible = info_button.collidepoint(event.pos)  # Info-Box anzeigen, wenn Maus über "i"

    # Beenden des Startbildschirms und nächstes Spiel starten
    pygame.quit()
    os.system(f"{sys.executable} {next_file}")
    sys.exit()

# Hauptprogramm
if __name__ == "__main__":
    pong_title_text = "Hallo {player_name}!"  # Begrüßung mit Spielernamen
    pong_instruction_text = "Das erste Spiel ist Pong"  # Einführungstext
    pong_info_text = [
        "Steuere den Schläger mit den Pfeiltasten.",
        "Halte den Ball im Spiel und sammle Punkte.",
        "Drücke den Start-Button, um zu beginnen.",
    ]
    
    start_screen(pong_title_text, pong_instruction_text, pong_info_text, "B_Mini_Game_Pia.py")

