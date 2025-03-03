import csv
import os

def save_game_score(player_name, score):
    csv_file = 'player_scores.csv'

    if os.path.isfile(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader]

            # Add the new player to the list
            rows.append({'Player': player_name, 'Score': str(score)})

            # Rank the players from highest to lowest score
            rows.sort(key=lambda x: int(x['Score']), reverse=True)

            # Delete the last players if there are more than 5 players
            if len(rows) > 5:
                rows = rows[:5]

        with open(csv_file, 'w', newline='') as file:
            fieldnames = ['Player', 'Score']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    else:
        with open(csv_file, 'w', newline='') as file:
            fieldnames = ['Player', 'Score']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Player': player_name, 'Score': str(score)})
