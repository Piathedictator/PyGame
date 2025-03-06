import pygame
import sys
import os
import Y_config

pygame.init()

# Fenstergröße
width, height = Y_config.WIDTH, Y_config.HEIGHT
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong - Startseite")

# Spielername aus Umgebungsvariable übernehmen
player_name = os.getenv("PLAYER_NAME", "Player")

# Hintergrundbild laden und skalieren
background = pygame.image.load("Z_background.jpg")
background = pygame.transform.scale(background, (width, height))

# Schriftarten
FONT_30 = pygame.font.Font(None, 30)
FONT_50 = pygame.font.Font(None, 50)
FONT_60 = pygame.font.Font(None, 60)

# Info-Symbol
info_button = pygame.Rect(width / 2 - 15, height / 2 + 75, 30, 30)

def start_screen(title_text, instructions_text, info_text, next_file):
    info_visible = False
    start_button = pygame.Rect(width / 2 - 75, height / 2, 150, 50)
    info_box = pygame.Rect(width / 2 - 240, height / 2 + 110, 480, 80)
    
    running = True
    while running:
        screen.blit(background, (0, 0))
        
        # Titel mit Schatten
        shadow_offset = 2
        title_shadow = FONT_60.render(title_text.format(player_name=player_name), True, Y_config.BLACK)
        screen.blit(title_shadow, (width / 2 - title_shadow.get_width() / 2 + shadow_offset, 150 + shadow_offset))
        title_surface = FONT_60.render(title_text.format(player_name=player_name), True, Y_config.CYAN)
        screen.blit(title_surface, (width / 2 - title_surface.get_width() / 2, 150))

        # Anleitung mit Schatten
        instructions_shadow = FONT_50.render(instructions_text, True, Y_config.BLACK)
        screen.blit(instructions_shadow, (width / 2 - instructions_shadow.get_width() / 2 + shadow_offset, 200 + shadow_offset))
        instructions_surface = FONT_50.render(instructions_text, True, Y_config.CYAN)
        screen.blit(instructions_surface, (width / 2 - instructions_surface.get_width() / 2, 200))
        
        # Anweisung um das Spiel freiwillig zu beenden
        exit_text = FONT_30.render("Drück Q um das Spiel zu beenden", True, Y_config.BLACK) 
        screen.blit(exit_text, (width / 2 - (exit_text.get_width()/2), 520))

        # Start-Button
        pygame.draw.rect(screen, Y_config.WHITE, start_button)
        button_text = FONT_60.render("Start", True, Y_config.BLACK)
        screen.blit(button_text, (width / 2 - button_text.get_width() / 2, height / 2 + 5))
        
        # Info-Symbol
        pygame.draw.circle(screen, Y_config.CYAN, info_button.center, 15)
        info_icon = FONT_50.render("i", True, Y_config.WHITE)
        screen.blit(info_icon, (info_button.x + 10, info_button.y))
        
        # Info-Text anzeigen, wenn aktiv
        if info_visible:
            pygame.draw.rect(screen, Y_config.YELLOW, info_box)
            for i, line in enumerate(info_text):
                text_surface = FONT_30.render(line, True, Y_config.CYAN)
                screen.blit(text_surface, (width / 2 - text_surface.get_width()/2, (height / 2 + 120) + i * 20))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Beenden mit Taste "Q"
                    pygame.quit()
                    exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    running = False
            if event.type == pygame.MOUSEMOTION:
                info_visible = info_button.collidepoint(event.pos)
    
    pygame.quit()
    os.system(f"{sys.executable} {next_file}")
    sys.exit()

if __name__ == "__main__":
    pong_title_text = "Hallo {player_name}!"
    pong_instruction_text = "Das erste Spiel ist Pong"
    pong_info_text = [
        "Steuere den Schläger mit den Pfeiltasten.",
        "Halte den Ball im Spiel und sammle Punkte.",
        "Drücke den Start-Button, um zu beginnen.",
    ]
    
    start_screen(pong_title_text, pong_instruction_text, pong_info_text, "B_Mini_Game_Pia.py")
