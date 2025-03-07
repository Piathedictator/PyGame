import pygame
import random
import os
import sys
import Y_config
from G_Game_Scores import save_game_score

# Punktestände und Spielername aus Umgebungsvariablen
score_pong = int(os.getenv("SCORE_PONG", "0"))
total_score_2048 = int(os.getenv("TOTAL_SCORE_2048", "0"))
score_snake = int(os.getenv("SCORE_SNAKE", "0"))
player_name = str(os.getenv("PLAYER_NAME", "PLAYER"))

# Gesamtpunktzahl berechnen und speichern
final_game_score = score_pong + total_score_2048 + score_snake
save_game_score(player_name, final_game_score)
os.environ["FINAL_GAME_SCORE"] = str(final_game_score)

# Fenster und Hintergrund
screen = Y_config.SCREEN
background = pygame.image.load("Z_background.jpg")
background = pygame.transform.scale(background, (Y_config.WIDTH, Y_config.HEIGHT))


# Spielnachrichten je nach Punktzahl
game_over_messages = {
    "low": 
    ["Das ist ja nicht so gut gelaufen.: Probier's nochmal!",
        "Anfängerfehler.: Jetzt streng dich mal an!",
        "Hätte hätte Snake Game Kette.: Da machste nix, probier's nochmal!",
        "Digga, dein Versagen kotzt mich an.: Vallah!",
        "Du hast verloren.: Geh nach Hause.",
        "Du hast schwach angefangen.: Dann stark nachgelassen!",
        "Loooooooser!!!",
        "Digga, was war das?!",
        "Spielst du mit den Füßen oder wat?",
        "Liegt dein Versagen am Spiel?: Ich denke nicht."],
    "medium": 
    [   "Ganz gut. Aber noch nicht genug!",
        "Na, das war schon besser.: Mehr Konzentration!",
        "Fast geschafft.: Aber noch ist nicht alles gewonnen!",
        "Mühlen mahlen langsam.: Deine Besonders.",
        "Gar nicht schlecht.: Hast du jemand dafür bezahlt?",
        "Ganz gut, aber da geht noch mehr!"],
    "high": 
    [   "Super! Das war richtig stark!",
        "Top Leistung! Fast perfekt!",
        "Du hast es richtig drauf!: Weiter so!",
        "Das war überraschend gut",
        "Weeeee are the champioooons.",
        "Unheimlich gut.",
        "Das war zu gut.: Hast du geschummelt?",
        "Na, bist du Teil der besten Liste?",]
}

def render_text_with_shadow(text, font, color, position):
    """Text mit Schatten rendern."""
    shadow_text = font.render(text, True, Y_config.SHADOW_COLOR)
    screen.blit(shadow_text, (position[0] + Y_config.SHADOW_OFFSET, position[1] + Y_config.SHADOW_OFFSET))
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def display_buttons():
    """Zeigt Buttons auf dem Bildschirm an."""
    restart_button = pygame.Rect(Y_config.WIDTH / 2 - 75, Y_config.HEIGHT / 2 + 70, 150, 50)
    score_button = pygame.Rect(Y_config.WIDTH / 2 - 100, Y_config.HEIGHT / 2 + 140, 200, 50)
    
    pygame.draw.rect(screen, Y_config.WHITE, restart_button)
    button_text1 = Y_config.FONT_60.render("Restart", True, Y_config.BLACK)
    screen.blit(button_text1, (Y_config.WIDTH / 2 - button_text1.get_width() / 2, Y_config.HEIGHT / 2 + 80))

    pygame.draw.rect(screen, Y_config.WHITE, score_button)
    button_text2 = Y_config.FONT_60.render("Bestenliste", True, Y_config.BLACK)
    screen.blit(button_text2, (Y_config.WIDTH / 2 - button_text2.get_width() / 2, Y_config.HEIGHT / 2 + 150))
    
    return restart_button, score_button

def start_screen(final_game_score):
    """Startbildschirm anzeigen."""
    # Nachricht je nach Punktzahl auswählen
    if final_game_score < 300:
        message_group = game_over_messages["low"]
    elif final_game_score < 500:
        message_group = game_over_messages["medium"]
    else:
        message_group = game_over_messages["high"]

    message = random.choice(message_group)
    parts = message.split(": ")

    running = True
    while running:
        screen.blit(background, (0, 0))

        # Endpunktestand anzeigen
        score_text = f"Endpunktestand: {final_game_score}"
        render_text_with_shadow(score_text, Y_config.FONT_60, Y_config.CYAN, (Y_config.WIDTH / 2 - Y_config.FONT_60.size(score_text)[0] / 2, 100))

        # Game Over Nachricht anzeigen
        for i, part in enumerate(parts):
            part_text = Y_config.FONT_40.render(part, True, Y_config.BLACK)
            screen.blit(part_text, (Y_config.WIDTH / 2 - part_text.get_width() / 2, 250 + i * 40))

        # Buttons anzeigen
        restart_button, score_button = display_buttons()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:  # Beenden mit "Q"
                pygame.quit()
                exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    command = "python3" if sys.platform != "win32" else "python"
                    os.system(f"{command} A_First_Page_generall.py")
                elif score_button.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    command = "python3" if sys.platform != "win32" else "python"
                    os.system(f"{command} F_Bestenliste.py")

start_screen(final_game_score)


