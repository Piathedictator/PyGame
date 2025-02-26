import pygame
from TEST_2_First_Page_Pia import start_screen  # Import the start_screen function from the first file

if __name__ == "__main__":
    # Custom information text to display on the start screen
    custom_info_text = [
        "Benutze die Pfeiltasten um die Zahlen zu verschieben.",
        "Gleiche Zahlen können durch Verschieben addiert werden",
    ]

    # Call the start_screen function and specify the next file to open
    start_screen(custom_info_text, "3_Mini_Game_Alvaro.py")  # Replace with the actual file you want to open
