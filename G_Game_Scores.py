import csv
import os

def save_game_score(player, scores=None):
    file_name = 'Storage_Game_Score.csv'  # Define the CSV file name
    file_exists = os.path.isfile(file_name)  # Check if the file exists to determine the mode

    # Initialize scores dictionary if not provided
    if scores is None:
        scores = {'Pong': 0, '2048': 0, 'Snake': 0}

    # Open the file in append mode, create it if it doesn't exist
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:  # Write the header only if the file is new
            writer.writerow(['player_name', 'Pong', '2048', 'Snake'])

        # Write the player's score, using the provided scores or default values
        writer.writerow([
            player,
            scores.get('Pong', 0),
            scores.get('2048', 0),
            scores.get('Snake', 0)
        ])