import pygame
import random
import os

pygame.init()

# Fenstergröße
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ende")

background = pygame.image.load("background_pong.jpg")  # Bild laden und anpassen
background = pygame.transform.scale(background, (width, height))

# Farben und Schriftarten
white = (255, 255, 255)
green = pygame.Color(0, 255, 0)  # Grüne Farbe für final_score

font_title = pygame.font.Font(None, 70)
font = pygame.font.Font(None, 50)
font_instruction = pygame.font.Font(None, 30)

def start_screen(final_score):
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
        "Fast geschafft.: Aber noch ist nicht alles gewonnen!"
    ]
    
    game_over_messages_high = [
        "Super!: Das war richtig stark!",
        "Top Leistung!: Fast perfekt!",
        "Du hast es richtig drauf!: Weiter so!"
    ]

    # Auswahl der richtigen Nachrichten basierend auf dem final_score
    if final_score < 100:
        message_group = game_over_messages_low
    elif final_score < 200:
        message_group = game_over_messages_medium
    else:
        message_group = game_over_messages_high

    # Zufällige Nachricht aus der ausgewählten Gruppe
    message = random.choice(message_group)
    parts = message.split(": ")  # Nachricht an ':' teilen

    start_button = pygame.Rect(width / 2 - 75, height / 2 + 100, 150, 50)  # Start-Button um 100 nach unten verschieben
    running = True

    while running:
        screen.blit(background, (0, 0))

        # Zeile für den final_score
        score_text = f"Endpunktestand:! {final_score}"

        # Zeilenumbruch in `score_text` einfügen
        score_lines = score_text.split("! ")  # Optional: wenn du nach "Dein Endpunktestand" und der Zahl trennen möchtest
        score_y = 100  # Startposition für die erste Zeile
        for line in score_lines:
            score_part = font_title.render(line, True, green)
            screen.blit(score_part, (width / 2 - score_part.get_width() / 2, score_y))
            score_y += 60  # Vertikaler Abstand für die nächste Zeile

        # Nachricht anzeigen (verschoben)
        for i, part in enumerate(parts):
            part_text = font_instruction.render(part, True, white)
            screen.blit(part_text, (width / 2 - part_text.get_width() / 2, 250 + i * 40))  # Nachrichten um 100 nach unten verschoben

        # Start Button (verschoben)
        pygame.draw.rect(screen, white, start_button)
        button_text = font.render("Restart", True, (0, 0, 0))
        screen.blit(button_text, (width / 2 - button_text.get_width() / 2, height / 2 + 110))  # Start-Button weiter nach unten verschoben

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                running = False

start_screen(150)  # Beispielaufruf mit einem final_score von 150

# Weiteres Spiel starten
os.system("python 1_First_Page_generall.py")
