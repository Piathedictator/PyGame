import csv
import os

def save_game_score(player_name, score):
    # Überprüfen, ob der Score gültig ist
    if score is None or not isinstance(score, (int, float)):
        score = 0  # Standardwert für ungültigen Score

    csv_file = 'player_scores.csv'

    try:
        # Überprüfen, ob die Datei existiert und wenn ja, die Datei lesen
        if os.path.isfile(csv_file):
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                rows = [row for row in reader]

            # Überprüfen, ob der Spieler bereits existiert
            if not any(row['Player'] == player_name for row in rows):
                rows.append({'Player': player_name, 'Score': str(score)})

            # Spieler nach Punktzahl sortieren (höchste Punktzahl zuerst)
            rows.sort(key=lambda x: int(x['Score']), reverse=True)

            # Wenn es mehr als 5 Spieler gibt, die Liste auf die Top 5 kürzen
            if len(rows) > 5:
                rows = rows[:5]

            # Datei überschreiben
            with open(csv_file, 'w', newline='') as file:
                fieldnames = ['Player', 'Score']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
        
        else:
            # Falls die Datei nicht existiert, eine neue Datei erstellen und den Spieler hinzufügen
            with open(csv_file, 'w', newline='') as file:
                fieldnames = ['Player', 'Score']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Player': player_name, 'Score': str(score)})

    except Exception as e:
        print(f"Fehler beim Zugriff auf die Datei: {e}")
