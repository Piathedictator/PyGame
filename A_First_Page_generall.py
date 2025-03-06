import pygame
import sys
import os
import csv
import subprocess
import Y_config
pygame.init()

# Fenstergröße
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Startseite_Python_Game")

# Hintergrundbild
background = pygame.image.load("Z_start_image.jpg")
background = pygame.transform.scale(background, (width, height))

# Farben & Schriftarten
white, pink, black, blue = (255, 255, 255), (251, 0, 255), (0, 0, 0), (173, 216, 230)
font = pygame.font.Font(None, 50)
font_titel = pygame.font.Font(None, 70)
font_instruction = pygame.font.Font(None, 30)

# UI-Elemente
input_box = pygame.Rect(width / 2 - 100, 250, 200, 40)
start_button = pygame.Rect(width / 2 - 100, 350, 200, 50)
info_button = pygame.Rect(width / 2 - 15, 420, 30, 30)
info_text = [
    "Spiele dich durch drei Mini-Spiele",
    "        und sammle Punkte!",
]

def check_player_name(name):
    try:
        with open('player_scores.csv', 'r') as file:
            reader = csv.reader(file)
            existing_names = [row[0] for row in reader]
            if name in existing_names:
                base_name, *suffix = name.rsplit(' ', 1)
                if suffix and suffix[0].isdigit():
                    new_name = f"{base_name} {int(suffix[0]) + 1}"
                else:
                    new_name = f"{name} 1"
                return check_player_name(new_name)
            else:
                return name
    except FileNotFoundError:
        return name

def start_screen():
    player_name = ""
    info_visible = False
    while True:
        screen.blit(background, (0, 0))
        
        titel_text = font_titel.render("Let's Play Python", True, pink)
        screen.blit(titel_text, (width / 2 - (titel_text.get_width()/2), 150))
        eingabe_text = font_instruction.render("Gib deinen Spielernamen ein:", True, pink)
        screen.blit(eingabe_text, (width / 2 - (eingabe_text.get_width()/2), 220))
        exit_text = font_instruction.render("Drück Q um das Spiel zu beenden", True, blue) 
        screen.blit(exit_text, (width / 2 - (exit_text.get_width()/2), 520))

        pygame.draw.rect(screen, white, input_box)
        screen.blit(font.render(player_name, True, black), (input_box.x + 10, input_box.y + 5))
        pygame.draw.rect(screen, white, start_button)
        screen.blit(font.render("Start Spiel", True, black), (start_button.x + 10, start_button.y + 10))

        pygame.draw.circle(screen, blue, info_button.center, 15)
        screen.blit(font.render("i", True, white), (info_button.x + 10, info_button.y))
        if info_visible:
            for i, line in enumerate(info_text):
                text_surface = font_instruction.render(line, True, white)
                screen.blit(text_surface, (width/ 2 - text_surface.get_width()/2, (height/2 +160) + i * 20))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Beenden mit Taste "Q"
                    pygame.quit()
                    exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == pygame.K_RETURN and player_name and len(player_name) <= 9:
                    final_player_name = check_player_name(player_name)
                    os.environ["PLAYER_NAME"] = str(final_player_name)
                    command = "python3" if sys.platform != "win32" else "python"
                    pygame.quit()
                    subprocess.call([command, "B_First_Page_Pia.py"])
                    sys.exit()
                elif len(player_name) < 9:  # Only add character if under limit
                    player_name += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos) and player_name:
                    final_player_name = check_player_name(player_name)
                    os.environ["PLAYER_NAME"] = str(final_player_name)
                    command = "python3" if sys.platform != "win32" else "python"
                    pygame.quit()
                    subprocess.call([command, "B_First_Page_Pia.py"])
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:
                info_visible = info_button.collidepoint(event.pos)

start_screen()