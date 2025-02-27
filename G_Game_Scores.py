import csv
import os

from A_First_Page_generall import player_name
from B
def save_game_score(player_name, game_name, score):
    file_name = 'Storage_Game_Score.csv'  # Define the CSV file name
    file_exists = os.path.isfile(file_name)  # Check if the file exists

    # Create a new row for the player and their score
    new_row = {
        'player_name': player_name,
        'Pong': 0,
        '2048': 0,
        'Snake': 0
    }
    new_row[game_name] = score  # Set the score for the specific game

    # Write the new row to the CSV file
    with open(file_name, mode='a', newline='') as file:  # Open in append mode
        writer = csv.DictWriter(file, fieldnames=['player_name', 'Pong', '2048', 'Snake'])
        if not file_exists:  # Write the header only if the file is new
            writer.writeheader()
        writer.writerow(new_row)  # Write the new player's score