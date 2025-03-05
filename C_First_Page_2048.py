import pygame
from B_First_Page_Pia import start_screen #loading function to display screen
import sys
import os

score_pong = int(os.getenv("SCORE_PONG", "0")) #loeading transition

if __name__ == "__main__":
    alvaro_title_text = f"Dein Score ist {score_pong}!" #title
    alvaro_instruction_text = "Das nächste Spiel ist 2048" #
    alvaro_info_text = [ # Info-Text
        "Benutze die Pfeiltasten, um Zahlen ", 
        "zu verschieben und gleiche zu addieren.",
        "Das Ziel ist es die Zahl 2048 erreichen.",
    ]
    start_screen(alvaro_title_text, alvaro_instruction_text, alvaro_info_text, "C_1_Mini_Game_Alvaro.py") # calling the function, start next file
