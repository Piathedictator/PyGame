import pygame

pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Startseite")

# Farben
white = (255, 255, 255)
blue = (173, 216, 230)
gray = (180, 180, 180)

# Schriftart
font = pygame.font.Font(None, 50)
font_instruction = pygame.font.Font(None, 30)
info_font = pygame.font.Font(None, 30)

# Info-Symbol
info_button = pygame.Rect(WIDTH / 2 - 15, HEIGHT/2 + 75, 30, 30)
info_visible = False
info_text = [
    "Steuere den Schläger mit den Pfeiltasten.",
    "Halte den Ball im Spiel und sammle Punkte.",
]

def start_screen():
    global info_visible
    start_button = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 2, 150, 50)
    running = True
    
    while running:
        screen.fill((0, 0, 0))
        
        #Titel:
        title_text = font.render("Willkommen zu Pong!", True, white)
        screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, 150))

        #Instuction Text:
        instructions_text = font_instruction.render("Drücke den Start-Button, um zu spielen.", True, white)
        screen.blit(instructions_text, (WIDTH / 2 - instructions_text.get_width() / 2, 200))
        
        #Start Button
        pygame.draw.rect(screen, white, start_button)
        button_text = font.render("Start", True, (0, 0, 0))
        screen.blit(button_text, (WIDTH / 2 - button_text.get_width() / 2, HEIGHT / 2 + 10))
        
        # Info-Symbol
        pygame.draw.circle(screen, blue, info_button.center, 15)
        info_icon = font.render("i", True, white)
        screen.blit(info_icon, (info_button.x + 10, info_button.y))
        
        # Info-Text anzeigen, wenn aktiv
        if info_visible:
            for i, line in enumerate(info_text):
                text_surface = info_font.render(line, True, white)
                screen.blit(text_surface, (WIDTH/ 2 - 200, (HEIGHT/2 +120) + i * 20))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                running = False
            if event.type == pygame.MOUSEMOTION:
                info_visible = info_button.collidepoint(event.pos)

start_screen()

import os
os.system("python Mini_Game_Pia.py")