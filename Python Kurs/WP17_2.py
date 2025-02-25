import matplotlib.pyplot as plt
import csv

# Datei einlesen und Daten verarbeiten
file_path = 'elections.csv'

years = []
parties = []
data = []

with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Erste Zeile (Kopfzeile)
    years = [row[0] for row in reader]  # Die Jahre
    parties = header[1:]  # Parteinamen (ohne Jahr-Spalte)
    
    # Daten erneut einlesen
    csvfile.seek(0)  # Zurück zum Anfang der Datei
    next(reader)  # Überspringe Kopfzeile
    for row in reader:
        data.append([float(value) if value else 0.0 for value in row[1:]])

# Farben für die Parteien definieren
colors = {
    'CDU/CSU': '#000000',  # Schwarz
    'SPD': '#FF0000',      # Rot
    'FDP': '#FFD700',      # Gelb
    'Grüne': '#008000',    # Grün
    'Linke': '#800080',    # Lila
    'AfD': '#1E90FF',      # Blau
    'Sonstige': '#C0C0C0'  # Grau
}

# Farben-Liste für Parteien in Reihenfolge
party_colors = [colors[party] for party in parties]

# Plot vorbereiten
fig, ax = plt.subplots(figsize=(10, 10))

# Radius der innersten Scheibe
radius_start = 0.3
width = 0.04

# Für jedes Jahr einen Ring erstellen
for i, (year, year_data) in enumerate(zip(years, data)):
    ax.pie(
        year_data,  # Daten des Jahres
        radius=radius_start + i * width,  # Radius für das aktuelle Jahr
        colors=party_colors,  # Farben entsprechend den Parteien
        labels=None if i != len(years)-1 else parties,  # Nur einmal Labels anzeigen
        startangle=0,  # Startwinkel
        wedgeprops=dict(width=width, edgecolor='w')  # Breite des Rings und Rand
    )

# Titel hinzufügen
plt.title("Deutsche Bundestagswahlen, 1949–2021 (Nested Pie)")

# Anzeige
plt.show()