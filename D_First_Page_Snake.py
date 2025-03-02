import os
import pygame
from B_First_Page_Pia import start_screen  # Import der Funktion, aber kein automatischer Aufruf mehr!
#from F_End_Page import total_score_2048

total_score_2048 = os.environ.get("TOTAL_SCORE_2048")

if __name__ == "__main__":
    # Benutzerdefinierter Info-Text
    snake_title_text = f"Dein Score ist {total_score_2048}!"
    snake_instruction_text = "Das nächste Spiel ist Snake"
    snake_info_text = [
        "Steuere die Schlange mit den Pfeiltasten.", 
        "Verschlinge die Früchte und sammle Punkte.",
    ]
    start_screen(snake_title_text, snake_instruction_text, snake_info_text, "D_1_Mini_Game_Frank.py") # Nächstes Spiel starten
