#WP10
#1
import math

while True:
    try:
        a = float(input("Give a value: "))
        b = float(input("Give a value: "))
        c = float(input("Give a value: "))
    except ValueError:
        print("Probier's nochmal.")
    else:
        break

    # Überprüfung der Sonderfälle

diskriminante = b**2 - 4 * a * c
    
    # Diskriminante überprüfen
if diskriminante > 0:
        # Zwei reale Lösungen
    x1 = (-b + math.sqrt(diskriminante)) / (2 * a)
    x2 = (-b - math.sqrt(diskriminante)) / (2 * a)
    print(f"Zwei Lösungen: x1 = {x1}, x2 = {x2}")
elif diskriminante == 0:
        # Eine doppelte Lösung
    x = -b / (2 * a)
    print(f"Eine doppelte Lösung: x = {x}")
else:
        # Komplexe Lösungen
    realteil = -b / (2 * a)
    imaginaerteil = math.sqrt(-diskriminante) / (2 * a)
    print(f"Zwei komplexe Lösungen: x1 = {realteil} + {imaginaerteil}i, x2 = {realteil} - {imaginaerteil}i")

#2
# Funktion, um einen neuen Score in die scores.txt Datei hinzuzufügen
def score_hinzufuegen(spieler_name, score):
    with open('scores.txt', 'a') as datei:  # öffnet die Datei "scores.txt" im Anhängemodus "a"
        datei.write(f"{spieler_name},{score}\n") # wird im Format Spielername, score gespeichert. \n sorgt für den Zeilumbruch

# Funktion, um die scores.txt Datei zu lesen und die Top 10 höchsten Scores zurückzugeben
def beste_scores():
    # Alle Zeilen aus der Datei lesen
    try:
        with open('scores.txt', 'r') as datei: #öffnen der Datei im Lesemodus "r"
            zeilen = datei.readlines()
    
    # Die Scores in einer Liste von Tupeln (name, score) speichern
        scores = []
        for zeile in zeilen:
            name, score = zeile.strip().split(',') #jede Zeile wird in zwei Teile aufgeteilt: den Namen des Spielers und den Score an der Stelle des Kommers.      
            try:
                score = int(zeile.strip().split(',')[1])
            except (ValueError, IndexError):
                print(f"{score} ist kein Integer.")
            else:    
                scores.append((name, int(score)))      #Die Daten werden als Tupel (name, score) in einer Liste scores gespeichert
    except FileNotFoundError:
        print()        
    # Die Scores nach der Punktzahl in absteigender Reihenfolge sortieren
    else:
        sortierte_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Die Top 10 Scores zurückgeben (oder weniger, wenn weniger als 10 Einträge vorhanden sind)
        return sortierte_scores[:10]

# Beispielaufruf:
# Einen neuen Score hinzufügen
score_hinzufuegen('Alice', 250)
score_hinzufuegen('Bob', 'Bert')
score_hinzufuegen('Charlie', 150)

# Die besten 10 Scores holen
top_scores = beste_scores()
print("Top 10 Scores:")
for i, (name, score) in enumerate(top_scores, 1): #i stellt die Platzierungen dar (beginnend bei 1) und enumerate loopt über die Tuples in der Liste der besten Scores.
    try:
        type(score) == int()
    except ValueError:
        print(f"{score} ist kein Integer.")
    else:
        print(f"{i}. {name}: {score}") # Gibt <= obersten 10 Tuple Päärchen wieder