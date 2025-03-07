import os
from B_First_Page_Pia import start_screen  # Import der Funktion

#Scores laden:
total_score_2048 = int(os.getenv("TOTAL_SCORE_2048", "0"))
score_pong = int(os.getenv("SCORE_PONG", "0"))
game_score_pong_2048 = total_score_2048 + score_pong

if __name__ == "__main__":
    # Benutzerdefinierter Info-Text
    snake_title_text = f"Dein Score ist {game_score_pong_2048}!"
    snake_instruction_text = "Das nächste Spiel ist Snake"
    snake_info_text = [
        "Steuere die Schlange mit den Pfeiltasten.", 
        "Verschlinge die Früchte und sammle Punkte.",
    ]
    start_screen(snake_title_text, snake_instruction_text, snake_info_text, "D_mini_game_Frank.py") # Nächstes Spiel starten
