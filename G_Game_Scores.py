import csv
import os


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
