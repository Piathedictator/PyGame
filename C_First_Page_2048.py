import pygame
from B_First_Page_Pia import start_screen   #, player_name
import sys
import os

#player_name = sys.argv[1]
#score_pong = sys.argv[2] if len(sys.argv) > 1 else "0"
score_pong = int(os.getenv("SCORE_PONG", "0"))

if __name__ == "__main__":
    # Benutzerdefinierter Info-Text
    alvaro_title_text = f"Dein Score ist {score_pong}!"
    alvaro_instruction_text = "Das nächste Spiel ist 2048"
    alvaro_info_text = [
        "Benutze die Pfeiltasten, um Zahlen ", 
        "zu verschieben und gleiche zu addieren.",
        "Das Ziel ist es die Zahl 2048 erreichen.",
    ]
    start_screen(alvaro_title_text, alvaro_instruction_text, alvaro_info_text, "C_1_Mini_Game_Alvaro.py") # Nächstes Spiel starten
