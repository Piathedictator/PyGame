import pygame
from B_First_Page_Pia import start_screen  # Import der Funktion, aber kein automatischer Aufruf mehr!

if __name__ == "__main__":
    # Benutzerdefinierter Info-Text
    custom_info_text = [
        "Benutze die Pfeiltasten, um die Zahlen zu verschieben.",
        "Gleiche Zahlen können durch Verschieben addiert werden.",
    ]
    start_screen(custom_info_text, "C.1_Mini_Game_Alvaro.py")  # Nächstes Spiel starten
