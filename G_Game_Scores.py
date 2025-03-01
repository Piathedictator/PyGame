import csv
import os

<<<<<<< HEAD
def save_game_score(player_name, score):
    csv_file = 'player_scores.csv' # Define the CSV file name

    player_exists = False # Initialize a flag to check if the player already exists

    if os.path.isfile(csv_file): # Check if the CSV file already exists
        with open(csv_file, 'r') as file: # Read the existing CSV file
            reader = csv.DictReader(file)
            rows = [row for row in reader]

            for row in rows: # Check if the player already exists
                if row['Player'] == player_name:
                    row['Score'] = str(int(row['Score']) + score) # Update the score if the player exists
                    player_exists = True
                    break

            if not player_exists: # If the player does not exist, add a new row
                rows.append({'Player': player_name, 'Score': str(score)})

        with open(csv_file, 'w', newline='') as file: # Write the updated rows back to the CSV file
            fieldnames = ['Player', 'Score']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    else: # Create a new CSV file if it does not exist
        with open(csv_file, 'w', newline='') as file:
            fieldnames = ['Player', 'Score']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Player': player_name, 'Score': str(score)})
=======

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
>>>>>>> parent of 535570a (Umbenennung Pages für Ende Page, End Page fertig bis auf die Score Variablen der einzelnen Games (total_score_20248 lässt sich nicht importieren)
