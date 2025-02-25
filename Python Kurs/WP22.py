#22.1
import pandas as pd

df = pd.read_csv('cities.csv')
            
# Überprüfe die ersten paar Zeilen der CSV, um sicherzustellen, dass die Daten korrekt eingelesen wurden
print(df.head())

max = df["City"][df["Population"].idxmax()]
min = df["City"][df["Population"].idxmin()]
#mean = df["City"][df["Population"].mean()] 

#print(f"Maximum={max}, Minimun={min}, Mittelwert={mean}")
print("")

#22.2
# Maximale Anzahl der Sitze
MAX_SEATS = 598

# Funktion zur Berechnung der Sitzverteilung
def calculate_seats(df):
    results = []
    
    for _, row in df.iterrows():
        year = int(row['Jahr'])  # "Jahr" unberührt lassen
        parties = row.drop('Jahr')  # Nur die Parteistimmen verarbeiten
        
        # Fehlende Werte (NaN) durch 0 ersetzen
        parties = parties.fillna(0)

        # Parteien mit weniger als 5% Stimmenanteil ausschließen
        valid_votes = parties[parties >= 5].sum()
        
        # Stimmenanteile für die qualifizierten Parteien berechnen
        if valid_votes > 0:
            seats = (parties / valid_votes) * MAX_SEATS
            seats[parties < 5] = 0  # Parteien mit < 5% erhalten 0 Sitze
        else:
            seats = parties * 0  # Alle Parteien erhalten 0 Sitze
        
        # Auf Ganzzahlen runden
        seats = seats.round().astype(int)
        
        # "Jahr" hinzufügen
        seats['Jahr'] = year
        results.append(seats)


 # Sicherstellen, dass "Jahr" die erste Spalte ist
    results_df = pd.DataFrame(results)
    results_df = results_df[['Jahr'] + [col for col in results_df.columns if col != 'Jahr']]
    return results_df

# Datei einlesen
elections_df = pd.read_csv('elections.csv')

# Sitzverteilung berechnen
seats_df = calculate_seats(elections_df)

# Ergebnis speichern
seats_df.to_csv('elections_seats.csv', index=False)


print(pd.read_csv('elections_seats.csv'))