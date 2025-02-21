import pygame
import sys
import os

pygame.init()

# Fenstergröße
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Startseite_Python_Game")

# Hintergrundbild
background = pygame.image.load("start_image.jpg")
background = pygame.transform.scale(background, (width, height))

# Farben & Schriftarten
white, pink, black, blue = (255, 255, 255), (251, 0, 255), (0, 0, 0), (173, 216, 230)
font = pygame.font.Font(None, 50)
font_titel = pygame.font.Font(None, 70)
font_instruction = pygame.font.Font(None, 30)

# UI-Elemente
input_box = pygame.Rect(width / 2 - 100, 250, 200, 40)
start_button = pygame.Rect(width / 2 - 75, 350, 150, 50)
info_button = pygame.Rect(width / 2 - 15, 420, 30, 30)
info_visible, player_name = False, ""
info_text = ["Spiele dich durch drei Mini-Spiele und sammle Punkte!"]

def start_screen():
    global info_visible, player_name
    while True:
        screen.blit(background, (0, 0))
        screen.blit(font_titel.render("Let's Play Python", True, pink), (width / 2 - 180, 150))
        screen.blit(font_instruction.render("Gib deinen Spielernamen ein:", True, pink), (width / 2 - 140, 220))
        pygame.draw.rect(screen, white, input_box)
        screen.blit(font.render(player_name, True, black), (input_box.x + 10, input_box.y + 5))
        pygame.draw.rect(screen, white, start_button)
        screen.blit(font.render("Start Spiel", True, black), (start_button.x + 10, start_button.y + 10))
        pygame.draw.circle(screen, blue, info_button.center, 15)
        screen.blit(font.render("i", True, white), (info_button.x + 10, info_button.y))
        if info_visible:
            screen.blit(font_instruction.render(info_text[0], True, white), (width / 2 - 200, 460))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == pygame.K_RETURN and player_name:
                    os.system(f"python 2_First_Page_Pia.py '{player_name}'")
                    return
                else:
                    player_name += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos) and player_name:
                    os.system(f"python 2_First_Page_Pia.py '{player_name}'")
                    return
                if info_button.collidepoint(event.pos):
                    info_visible = not info_visible
            if event.type == pygame.MOUSEMOTION:
                info_visible = info_button.collidepoint(event.pos)

start_screen()