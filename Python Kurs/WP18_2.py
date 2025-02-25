import pandas as pd
import matplotlib.pyplot as plt

# Lade die Datei und stelle sicher, dass sie durch Kommata getrennt wird
df = pd.read_csv('cities.csv')

# Überprüfe die ersten paar Zeilen der CSV, um sicherzustellen, dass die Daten korrekt eingelesen wurden
print(df.head())

# Sicherstellen, dass die Spaltennamen korrekt sind
df.columns = ['City', 'Population', 'Latitude', 'Longitude']

# Konvertiere die Spalten für Latitude und Longitude in den richtigen Datentyp
df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

# Skalierung der Punktgröße (z.B. Population in einen Bereich von 10 bis 300 skalieren)
population_scaled = df['Population'] / df['Population'].max() * 300

# Falls wir keine Fläche haben, können wir die Bevölkerungsdichte nicht berechnen, daher visualisieren wir einfach die Städte
plt.figure(figsize=(10, 8))


# Streudiagramm der Städte mit Punktgröße proportional zur Bevölkerung
scatter = plt.scatter(df['Longitude'], df['Latitude'], c=df['Population'], cmap='viridis', s=population_scaled, alpha=0.7, edgecolors='k')

# Füge eine Farbskala hinzu, um die Bevölkerung darzustellen
plt.colorbar(scatter, label='Bevölkerung')

# Achsenbeschriftungen und Titel
plt.xlabel('Längengrad')
plt.ylabel('Breitengrad')
plt.title('Deutsche Städte: Bevölkerung')

# Seitenverhältnis anpassen, um das Land korrekt darzustellen
plt.gca().set_aspect(1.4, adjustable='box')

# Zeige das Streudiagramm an
plt.show()
