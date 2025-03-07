import pygame
import sys
import os
import csv
import subprocess
import Y_config
pygame.init()

# Fenstergröße & Bildschirm
width, height = Y_config.WIDTH, Y_config.HEIGHT
screen = Y_config.SCREEN
pygame.display.set_caption("Startseite_Python_Game")

# Hintergrundbild
background = pygame.transform.scale(pygame.image.load("Z_start_image.jpg"), (width, height))


# UI-Elemente
input_box = pygame.Rect(width / 2 - 100, 250, 200, 40)
start_button = pygame.Rect(width / 2 - 100, 350, 200, 50)
info_button = pygame.Rect(width / 2 - 15, 410, 30, 30)
info_text = ["Spiele dich durch drei Mini-Spiele", "        und sammle Punkte!"]


def render_text_with_shadow(text, font, color, shadow_color, pos, offset=2):
    shadow = font.render(text, True, shadow_color)
    screen.blit(shadow, (pos[0] + offset, pos[1] + offset))
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)


def check_player_name(name):
    try:
        with open("player_scores.csv", "r") as file:
            existing_names = {row[0] for row in csv.reader(file)}
        while name in existing_names:
            base_name, *suffix = name.rsplit(" ", 1)
            name = f"{base_name} {int(suffix[0]) + 1}" if suffix and suffix[0].isdigit() else f"{name} 1"
    except FileNotFoundError:
        pass
    return name


def draw_ui(player_name, info_visible):
    screen.blit(background, (0, 0))
    render_text_with_shadow("Let's Play Python", Y_config.FONT_70, Y_config.CYAN, Y_config.BLACK, (width / 2 - Y_config.FONT_70.size("Let's Play Python")[0] / 2, 150))
    render_text_with_shadow("Gib deinen Spielernamen ein:", Y_config.FONT_30, Y_config.CYAN, Y_config.BLACK, (width / 2 - Y_config.FONT_30.size("Gib deinen Spielernamen ein:")[0] / 2, 220))
    screen.blit(Y_config.FONT_30.render("Drück Q um das Spiel zu beenden", True, Y_config.CYAN), (30, 570))
    
    pygame.draw.rect(screen, Y_config.WHITE, input_box)
    screen.blit(Y_config.FONT_50.render(player_name, True, Y_config.BLACK), (input_box.x + 10, input_box.y + 5))
    pygame.draw.rect(screen, Y_config.WHITE, start_button)
    screen.blit(Y_config.FONT_50.render("Start Spiel", True, Y_config.BLACK), (start_button.x + 10, start_button.y + 10))
    
    pygame.draw.circle(screen, Y_config.BLACK, info_button.center, 15)
    screen.blit(Y_config.FONT_50.render("i", True, Y_config.WHITE), (info_button.x + 10, info_button.y))
    
    if info_visible:
        box_width, box_height = 400, 60
        box_x, box_y = (width - box_width) / 2, (height / 2 + 150)
        pygame.draw.rect(screen, Y_config.WHITE, (box_x, box_y, box_width, box_height))
        for i, line in enumerate(info_text):
            screen.blit(Y_config.FONT_30.render(line, True, Y_config.BLACK), (width / 2 - Y_config.FONT_30.size(line)[0] / 2, (height / 2 + 160) + i * 20))
    
    pygame.display.flip()


def start_game(player_name):
    os.environ["PLAYER_NAME"] = check_player_name(player_name)
    pygame.quit()
    subprocess.call(["python3" if sys.platform != "win32" else "python", "B_First_Page_Pia.py"])
    sys.exit()


def start_screen():
    player_name, info_visible = "", False
    
    while True:
        draw_ui(player_name, info_visible)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == pygame.K_RETURN and player_name:
                    start_game(player_name)
                elif len(player_name) < 9:
                    player_name += event.unicode
            
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos) and player_name:
                start_game(player_name)
            
            if event.type == pygame.MOUSEMOTION:
                info_visible = info_button.collidepoint(event.pos)


start_screen()
