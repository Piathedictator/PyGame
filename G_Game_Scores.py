import csv
import os


def save_game_score(player_name, Total_Game_Score):
    file_name = 'Storage_Game_Score.csv'  # Define the CSV file name
    file_exists = os.path.isfile(file_name)  # Check if the file exists

    # Create a new row for the player and their score
    new_row = {'player_name': player_name, Total_Game_Score: 0}

    # Write the new row to the CSV file
    with open(file_name, mode='a', newline='') as file:  # Open in append mode
        writer = csv.DictWriter(file, fieldnames=['player_name', 'Pong', '2048', 'Snake'])
        if not file_exists:  # Write the header only if the file is new
            writer.writeheader()
        writer.writerow(new_row)  # Write the new player's score