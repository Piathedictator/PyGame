import pygame
import sys
import os

pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Startseite")

# Spielername aus Umgebungsvariable übernehmen
player_name = os.getenv("PLAYER_NAME", "Player")

# Hintergrundbild laden und skalieren
background = pygame.image.load("Z_background_pages.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Farben
WHITE, BLUE, GRAY, PINK, YELLOW, BLACK = (
    (255, 255, 255), (173, 216, 230), (180, 180, 180),
    (255, 0, 255), (255, 255, 102), (0, 0, 0)
)

# Schriftarten
FONT = pygame.font.Font(None, 60)
FONT_INSTRUCTION = pygame.font.Font(None, 50)
INFO_FONT = pygame.font.Font(None, 30)

# Info-Symbol
info_button = pygame.Rect(WIDTH / 2 - 15, HEIGHT / 2 + 75, 30, 30)

def start_screen(title_text, instructions_text, info_text, next_file):
    info_visible = False
    start_button = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 2, 150, 50)
    info_box = pygame.Rect(WIDTH / 2 - 240, HEIGHT / 2 + 110, 480, 80)
    
    running = True
    while running:
        screen.blit(background, (0, 0))
        
        # Titel mit Schatten
        shadow_offset = 2
        title_shadow = FONT.render(title_text.format(player_name=player_name), True, BLACK)
        screen.blit(title_shadow, (WIDTH / 2 - title_shadow.get_width() / 2 + shadow_offset, 150 + shadow_offset))
        title_surface = FONT.render(title_text.format(player_name=player_name), True, PINK)
        screen.blit(title_surface, (WIDTH / 2 - title_surface.get_width() / 2, 150))

        # Anleitung mit Schatten
        instructions_shadow = FONT_INSTRUCTION.render(instructions_text, True, BLACK)
        screen.blit(instructions_shadow, (WIDTH / 2 - instructions_shadow.get_width() / 2 + shadow_offset, 200 + shadow_offset))
        instructions_surface = FONT_INSTRUCTION.render(instructions_text, True, PINK)
        screen.blit(instructions_surface, (WIDTH / 2 - instructions_surface.get_width() / 2, 200))
        
        # Start-Button
        pygame.draw.rect(screen, YELLOW, start_button)
        button_text = FONT.render("Start", True, PINK)
        screen.blit(button_text, (WIDTH / 2 - button_text.get_width() / 2, HEIGHT / 2 + 5))
        
        # Info-Symbol
        pygame.draw.circle(screen, BLUE, info_button.center, 15)
        info_icon = FONT_INSTRUCTION.render("i", True, WHITE)
        screen.blit(info_icon, (info_button.x + 10, info_button.y))
        
        # Info-Text anzeigen, wenn aktiv
        if info_visible:
            pygame.draw.rect(screen, YELLOW, info_box)
            for i, line in enumerate(info_text):
                text_surface = INFO_FONT.render(line, True, PINK)
                screen.blit(text_surface, (WIDTH / 2 - text_surface.get_width()/2, (HEIGHT / 2 + 120) + i * 20))
        
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
