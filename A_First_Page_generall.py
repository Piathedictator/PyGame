import pygame
import sys
import os
import csv
import subprocess
import Y_config

pygame.init()

# Fenstergröße & Bildschirm setzen
width, height = Y_config.WIDTH, Y_config.HEIGHT
screen = Y_config.SCREEN
pygame.display.set_caption("Startseite_Python_Game")

# Hintergrundbild laden und skalieren
background = pygame.transform.scale(pygame.image.load("Z_start_image.jpg"), (width, height))

# UI-Elemente (Eingabefeld, Buttons)
input_box = pygame.Rect(width / 2 - 100, 250, 200, 40)  # Eingabefeld für den Spielernamen
start_button = pygame.Rect(width / 2 - 100, 350, 200, 50)  # Start-Button
info_button = pygame.Rect(width / 2 - 15, 410, 30, 30)  # Info-Button ("i")

# Texte für die UI
title_text = "Let's Play Python"
name_prompt_text = "Gib deinen Spielernamen ein:"
quit_text = "Drück Q um das Spiel zu beenden"
start_button_text = "Start Spiel"
info_text = ["Spiele dich durch drei Mini-Spiele", "        und sammle Punkte!"]
info_button_text = "i"

# Funktion zum Rendern von Text mit Schatten
def render_text(text, font, color, shadow_color, pos, offset=2):
    shadow = font.render(text, True, shadow_color)  # Schattentext rendern
    screen.blit(shadow, (pos[0] + offset, pos[1] + offset))  # Schatten leicht versetzt zeichnen
    screen.blit(font.render(text, True, color), pos)  # Haupttext rendern

# Funktion zur Überprüfung und Anpassung des Spielernamens
def check_player_name(name):
    try:
        with open("player_scores.csv", "r") as file:
            existing_names = {row[0] for row in csv.reader(file)}  # Existierende Namen aus CSV-Datei einlesen
        
        # Falls der Name bereits existiert, eine Nummer anhängen
        while name in existing_names:
            base_name, *suffix = name.rsplit(" ", 1)
            name = f"{base_name} {int(suffix[0]) + 1}" if suffix and suffix[0].isdigit() else f"{name} 1"
    except FileNotFoundError:
        pass  # Falls Datei nicht existiert, einfach den ursprünglichen Namen behalten
    return name

# Funktion zum Zeichnen der UI
def draw_ui(player_name, info_visible):
    screen.blit(background, (0, 0))  # Hintergrundbild zeichnen

    # Titel mit Schatten rendern
    render_text(title_text, Y_config.FONT_70, Y_config.CYAN, Y_config.BLACK, 
                (width / 2 - Y_config.FONT_70.size(title_text)[0] / 2, 150))
    
    # Eingabeaufforderung für den Namen mit Schatten rendern
    render_text(name_prompt_text, Y_config.FONT_30, Y_config.CYAN, Y_config.BLACK, 
                (width / 2 - Y_config.FONT_30.size(name_prompt_text)[0] / 2, 220))
    
    # Hinweistext zum Beenden des Spiels
    screen.blit(Y_config.FONT_30.render(quit_text, True, Y_config.CYAN), (30, 570))

    # Eingabefeld für den Spielernamen zeichnen
    pygame.draw.rect(screen, Y_config.WHITE, input_box)
    screen.blit(Y_config.FONT_50.render(player_name, True, Y_config.BLACK), (input_box.x + 10, input_box.y + 5))
    
    # Start-Button zeichnen
    pygame.draw.rect(screen, Y_config.WHITE, start_button)
    screen.blit(Y_config.FONT_50.render(start_button_text, True, Y_config.BLACK), 
                (start_button.x + 10, start_button.y + 10))
    
    # Info-Button (schwarzer Kreis mit weißem "i") zeichnen
    pygame.draw.circle(screen, Y_config.BLACK, info_button.center, 15)
    screen.blit(Y_config.FONT_50.render(info_button_text, True, Y_config.WHITE), (info_button.x + 10, info_button.y))
    
    # Falls die Maus über den Info-Button fährt, die Infobox anzeigen
    if info_visible:
        box_width, box_height = 400, 60  # Größe der Infobox
        box_x, box_y = (width - box_width) / 2, (height / 2 + 150)  # Position der Infobox
        pygame.draw.rect(screen, Y_config.WHITE, (box_x, box_y, box_width, box_height))  # Weiße Box zeichnen
        
        # Info-Text in der Box anzeigen
        for i, line in enumerate(info_text):
            screen.blit(Y_config.FONT_30.render(line, True, Y_config.BLACK), 
                        (width / 2 - Y_config.FONT_30.size(line)[0] / 2, (height / 2 + 160) + i * 20))

    pygame.display.flip()  # Bildschirm aktualisieren

# Funktion zum Starten des Spiels
def start_game(player_name):
    os.environ["PLAYER_NAME"] = check_player_name(player_name)  # Spielernamen speichern
    pygame.quit()  # Pygame beenden
    subprocess.call(["python3" if sys.platform != "win32" else "python", "B_First_Page_Pia.py"])  # Neues Skript starten
    sys.exit()  # Programm beenden

# Hauptfunktion für den Startbildschirm
def start_screen():
    player_name, info_visible = "", False  # Initialisierung von Variablen

    while True:
        draw_ui(player_name, info_visible)  # UI zeichnen
        
        for event in pygame.event.get():
            # Beenden des Spiels mit dem Schließen-Button oder der "Q"-Taste
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            
            # Tastatureingaben verarbeiten
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:  # Löschen eines Zeichens im Namen
                    player_name = player_name[:-1]
                elif event.key == pygame.K_RETURN and player_name:  # Spiel starten, wenn Enter gedrückt wird
                    start_game(player_name)
                elif len(player_name) < 9:  # Zeichen zur Namenseingabe hinzufügen (maximal 9 Zeichen)
                    player_name += event.unicode
            
            # Start-Button anklicken, um das Spiel zu starten
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos) and player_name:
                start_game(player_name)
            
            # Überprüfen, ob die Maus über dem Info-Button ist
            if event.type == pygame.MOUSEMOTION:
                info_visible = info_button.collidepoint(event.pos)

start_screen()  # Startbildschirm aufrufen
