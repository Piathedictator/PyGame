import pygame
from B_First_Page_Pia import start_screen  # Import der Funktion, aber kein automatischer Aufruf mehr!

if __name__ == "__main__":
    # Benutzerdefinierter Info-Text
    alvaro_title_text = "Das nächste Spiel ist 2048!"
    alvaro_instruction_text = "Klicke auf Start um zu beginnen"
    alvaro_info_text = [
        "Benutze die Pfeiltasten, um Zahlen ", 
        "zu verschieben und gleiche zu addieren.",
        "Das Ziel ist es die Zahl 2048 erreichen.",
    ]
    start_screen(alvaro_title_text, alvaro_instruction_text, alvaro_info_text, "C.1_Mini_Game_Alvaro.py") # Nächstes Spiel starten
