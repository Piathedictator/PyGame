import pygame
import sys
import os

pygame.init()

# Fenstergröße
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong - Startseite")

# Player Name aus Skript übernehmen
#player_name = sys.argv[1] if len(sys.argv) > 1 else "Player"
player_name = os.getenv("PLAYER_NAME", "0")

background = pygame.image.load("Z_background_pages.jpg")  # Bild laden
background = pygame.transform.scale(background, (width, height))  # Größe anpassen

# Farben
white = (255, 255, 255)
blue = (173, 216, 230)
gray = (180, 180, 180)
pink = (255, 0, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)  # Für Schatten

# Schriftart
font = pygame.font.Font(None, 60)
font_instruction = pygame.font.Font(None, 50)
info_font = pygame.font.Font(None, 30)

# Info-Symbol
info_button = pygame.Rect(width / 2 - 15, height / 2 + 75, 30, 30)

def start_screen(titel_text, instructions_text, info_text, next_file):
    info_visible = False
    start_button = pygame.Rect(width / 2 - 75, height / 2, 150, 50)
    info_box = pygame.Rect(width / 2 - 240, height / 2 + 110, 480, 80)
    running = True
    
    while running:
        screen.blit(background, (0, 0))
        
        # Titel mit Schatten
        shadow_offset = 2
        title_text_shadow = font.render(titel_text.format(player_name=player_name), True, black)
        screen.blit(title_text_shadow, (width / 2 - title_text_shadow.get_width() / 2 + shadow_offset, 150 + shadow_offset))
        title_text = font.render(titel_text.format(player_name=player_name), True, pink)
        screen.blit(title_text, (width / 2 - title_text.get_width() / 2, 150))

        # Instruction Text mit Schatten
        instructions_text_shadow = font_instruction.render(instructions_text, True, black)
        screen.blit(instructions_text_shadow, (width / 2 - instructions_text_shadow.get_width() / 2 + shadow_offset, 200 + shadow_offset))
        instructions_text_surface = font_instruction.render(instructions_text, True, pink)
        screen.blit(instructions_text_surface, (width / 2 - instructions_text_surface.get_width() / 2, 200))
        
        # Start Button
        pygame.draw.rect(screen, yellow, start_button)
        button_text = font.render("Start", True, pink)
        screen.blit(button_text, (width / 2 - button_text.get_width() / 2, height / 2 + 5))
        
        # Info-Symbol
        pygame.draw.circle(screen, blue, info_button.center, 15)
        info_icon = font_instruction.render("i", True, white)
        screen.blit(info_icon, (info_button.x + 10, info_button.y))
        
        # Info-Text anzeigen, wenn aktiv
        if info_visible:
            pygame.draw.rect(screen, yellow, info_box)
            for i, line in enumerate(info_text):
                text_surface = info_font.render(line, True, pink)
                screen.blit(text_surface, (width / 2 - text_surface.get_width()/2, (height / 2 + 120) + i * 20))
        
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

if __name__ == "__main__":
    pong_title_text = "Hallo {player_name}!"
    pong_instruction_text = "Das erste Spiel ist Pong"
    pong_info_text = [
        "Steuere den Schläger mit den Pfeiltasten.",
        "Halte den Ball im Spiel und sammle Punkte.",
        "Drücke den Start-Button, um zu beginnen.",
    ]
    
    start_screen(pong_title_text, pong_instruction_text, pong_info_text, "B_1_Mini_Game_Pia.py")

