import pygame
import random
import os
import sys
from G_Game_Scores import save_game_score

# Übergeben der Scores der einzelnen Mini Games. Sicherstellen, dass fehlende Werte auf 0 gesetzt werden
score_pong = int(os.getenv("SCORE_PONG", "0"))
total_score_2048 = int(os.getenv("TOTAL_SCORE_2048", "0"))
score_snake = int(os.getenv("SCORE_SNAKE", "0"))
player_name = str(os.getenv("PLAYER_NAME", "PLAYER"))

# Gesamtpunktzahl berechnen
final_game_score = score_pong + total_score_2048 + score_snake

save_game_score(player_name, final_game_score)
os.environ["FINAL_GAME_SCORE"] = str(final_game_score)

pygame.init()

# Fenstergröße
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ende")

background = pygame.image.load("Z_background_pong.jpg")  # Bild laden und anpassen
background = pygame.transform.scale(background, (width, height))

# Farben und Schriftarten
white = (255, 255, 255)
green = pygame.Color(0, 255, 0)  # Grüne Farbe für final_game_score

font_title = pygame.font.Font(None, 70)
font = pygame.font.Font(None, 50)
font_instruction = pygame.font.Font(None, 30)


def start_screen(final_game_score):
    # Game Over Nachrichten für unterschiedliche Punktzahlen
    game_over_messages_low = [
        "Das ist ja nicht so gut gelaufen.: Probier's nochmal!",
        "Anfängerfehler.: Jetzt streng dich mal an!",
        "Hätte hätte Snake Game Kette.: Da machste nix, probier's nochmal!",
        "Digga, dein Versagen kotzt mich an.: Vallah!",
        "Du hast verloren.: Geh nach Hause.",
        "Du hast schwach angefangen.: Dann stark nachgelassen!",
        "Loooooooser!!!",
        "Digga, was war das?!",
        "Spielst du mit den Füßen oder wat?",
        "Liegt dein Versagen am Spiel?: Ich denke nicht."
    ]
    
    game_over_messages_medium = [
        "Ganz gut.: Aber noch nicht genug!",
        "Na, das war schon besser.: Mehr Konzentration!",
        "Fast geschafft.: Aber noch ist nicht alles gewonnen!",
        "Mühlen mahlen langsam. Deine Besonders.",
        "Gar nicht schlecht. Hast du jemand dafür bezahlt?",
        "Ganz gut, aber da geht noch mehr!"
    ]
    
    game_over_messages_high = [
        "Super!: Das war richtig stark!",
        "Top Leistung!: Fast perfekt!",
        "Du hast es richtig drauf!: Weiter so!",
        "Das war überraschend gut",
        "Weeeee are the champioooons.",
        "Unheimlich gut.",
        "Das war zu gut. Hast du geschummelt?",
        "Na, bist du Teil der besten Liste?",
    ]

    # Auswahl der richtigen Nachrichten basierend auf dem final_game_score
    if final_game_score < 100:
        message_group = game_over_messages_low
    elif final_game_score < 200:
        message_group = game_over_messages_medium
    else:
        message_group = game_over_messages_high

    # Zufällige Nachricht aus der ausgewählten Gruppe
    message = random.choice(message_group)
    parts = message.split(": ")  # Nachricht an ':' teilen

    restart_button = pygame.Rect(width / 2 - 75, height / 2 + 70, 150, 50)  # Restart-Button
    running = True

    score_button = pygame.Rect(width / 2 - 100, height / 2 + 140, 200, 50)  # Score-Button
    running = True

    while running:
        screen.blit(background, (0, 0))

        # Zeile für den final_game_score
        score_text = f"Endpunktestand:! {final_game_score}"

        # Zeilenumbruch in `score_text` einfügen
        score_lines = score_text.split("! ")  # Optional: wenn du nach "Dein Endpunktestand" und der Zahl trennen möchtest
        score_y = 100  # Startposition für die erste Zeile
        for line in score_lines:
            score_part = font_title.render(line, True, green)
            screen.blit(score_part, (width / 2 - score_part.get_width() / 2, score_y))
            score_y += 60  # Vertikaler Abstand für die nächste Zeile

        # Nachricht anzeigen
        for i, part in enumerate(parts):
            part_text = font_instruction.render(part, True, white)
            screen.blit(part_text, (width / 2 - part_text.get_width() / 2, 250 + i * 40))  # Nachrichten um 100 nach unten verschoben

        # Restart Button
        pygame.draw.rect(screen, white, restart_button)
        button_text1 = font.render("Restart", True, (0, 0, 0))
        screen.blit(button_text1, (width / 2 - button_text1.get_width() / 2, height / 2 + 80))  # Start-Button weiter nach unten verschoben

        # Score Button
        
        pygame.draw.rect(screen, white, score_button)
        button_text2 = font.render("Bestenliste", True, (0, 0, 0))
        screen.blit(button_text2, (width / 2 - button_text2.get_width() / 2, height / 2 + 150))  # Start-Button weiter nach unten verschoben
    

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and restart_button.collidepoint(event.pos):
                running = False
                # Weiteres Spiel starten
                command = "python3" if sys.platform != "win32" else "python"
                os.system(f"{command} A_First_Page_generall.py")
            if event.type == pygame.MOUSEBUTTONDOWN and score_button.collidepoint(event.pos):
                running = False
                # Weiteres Spiel starten
                command = "python3" if sys.platform != "win32" else "python"
                os.system("f {command} F_Game_scores.py")
start_screen(final_game_score)  # Beispielaufruf mit einem final_game_score von 150


