#WP20
import numpy as np

#20.1: Daten darstellen und Kombinationen berechnen

# Gegebene Daten
prices = np.array([1.0, 0.9, 2.3, 1.5, 0.3])  # Preis pro Einheit
scores = np.array([5, 4, 12, 7, 1])            # Score pro Einheit
budget = 10.0                                  # Budget in Euro

# Schritt 1: Maximale Einheiten berechnen. Bsp. Für „Dunkle Schokolade“ mit einem Preis von 1€ ergibt sich max_units[0]=⌊10/1⌋=10.
max_units = np.floor(budget / prices).astype(int) 
print("Maximale Einheiten pro Produkt:", max_units)

# Schritt 2: Alle möglichen Kombinationen generieren
ranges = [np.arange(0, m + 1) for m in max_units]  # Von 0 bis maximale Einheiten pro Produkt. ranges erstellt Listen von möglichen Stückzahlen für jede Süßigkeit
combinations = np.array(np.meshgrid(*ranges)).T.reshape(-1, len(prices)) #np.meshgrid kombiniert diese Listen zu einem Gitter, das alle möglichen Kombinationen darstellt.
print("Anzahl der Kombinationen:", combinations.shape[0]) #reshape formatiert das Ergebnis in eine Liste aller Kombinationen.
#Es entstehen 157,080 Kombinationen

#Aufgabe 20.2: Kombinationen bewerten und optimale Lösung finden

# Schritt 3: Gesamtpreis und Gesamtscore für jede Kombination berechnen
total_prices = np.sum(combinations * prices, axis=1)
total_scores = np.sum(combinations * scores, axis=1)

# Schritt 4: Kombinationen, die das Budget überschreiten, mit Score = -1 markieren
total_scores[total_prices > budget] = -1

# Schritt 5: Beste Kombination finden
max_score_index = np.argmax(total_scores)  # Index des höchsten Scores
max_score_combination = combinations[max_score_index]  # Beste Kombination
max_score = total_scores[max_score_index]  # Höchster Score

# Ergebnisse ausgeben
print("Beste Kombination (Anzahl Einheiten pro Produkt):", max_score_combination)
print("Höchster Score:", max_score)
