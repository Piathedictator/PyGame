import csv
import os

def save_game_score(player_name, pong_score, game2048_score, snake_score):
    file_name = 'Storage_Game_Score.csv' # Define the CSV file name
    file_exists = os.path.isfile(file_name) # Check if the file exists to determine the mode

    with open(file_name, mode='a', newline='') as file: # Open the file in append mode, create it if it doesn't exist
        writer = csv.writer(file)

        if not file_exists:  # Write the header only if the file is new
            writer.writerow(['player_name', 'Pong', '2048', 'Snake'])
        writer.writerow([player_name, pong_score, game2048_score, snake_score]) # Write the player's score