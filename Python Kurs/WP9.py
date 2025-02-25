#WP 9
#9.1
def sieve_of_eratosthenes(N):
    # Schritt 1: Erstellle eine Liste mit allen Primzahlen bis N
    is_prime = [True] * (N + 1)  # Alle Einträge sind zunächst als Primzahlen markiert
    is_prime[0] = False  # 0 ist keine Primzahl
    is_prime[1] = False  # 1 ist keine Primzahl
    
    # Schritt 2: die kleinste übrige Primzahl p ist 2
    p = 2
    while p * p <= N:
        # Schritt 3: markiere alle vielfachen von p (außer p) als KEINE Primzahlen
        if is_prime[p]:  # markiere nur die Vielfachen, falls p immer noch eine Primzahl ist
            for multiple in range(p * p, N + 1, p):  #Start bei p hoch 2; endet bei N + 1, da bei ansonsten die Schleife vor dem errreich von N stoppt und nicht nach dem erreichen von N; die Schrittweite zwischen Start und Stoppunkt ist p
                is_prime[multiple] = False           # Vielfaches vom aktuellen p wird als KEINE Primzahl markiert
        # Schritt 4: Finde die nächste Primzahl.
        p += 1   # Sollte nach diesem Schritt p keine Primzahl mehr sein, dann wird dieser Schritt solange wiederholt bis p wieder eine markierte Primzahl ist. Die vorherige Schleife zur Markierung alle Vielfachen von p als Primzahl wird dann wiederholt.
    
    # Schritt: Sammle alle Zahlen, die immernoch als Primzahlen markiert sind und extrahiere diese. Gibt eine in jeder Zeile wieder, ob eine Zahl aus is_prime eine Primzahl ist(True).
    primes = [num for num, prime in enumerate(is_prime) if prime]  # enumerate ist eine kompakte Listenkomprehensions Methode. Der Code nimmt jeden Eintragl(num) in is_prime in eine neu Liste auf, solange die Bedingung if prime is True gilt.
    return primes

N = 30 # Beispiel
print(sieve_of_eratosthenes(N))  

#9.2
# Funktion, um einen neuen Score in die scores.txt Datei hinzuzufügen
def score_hinzufuegen(spieler_name, score):
    with open('scores.txt', 'a') as datei:  # öffnet die Datei "scores.txt" im Anhängemodus "a"
        datei.write(f"{spieler_name},{score}\n") # wird im Format Spielername, score gespeichert. \n sorgt für den Zeilumbruch

# Funktion, um die scores.txt Datei zu lesen und die Top 10 höchsten Scores zurückzugeben
def beste_scores():
    # Alle Zeilen aus der Datei lesen
    with open('scores.txt', 'r') as datei: #öffnen der Datei im Lesemodus "r"
        zeilen = datei.readlines()

    # Die Scores in einer Liste von Tupeln (name, score) speichern
    scores = []
    for zeile in zeilen:
        name, score = zeile.strip().split(',') #jede Zeile wird in zwei Teile aufgeteilt: den Namen des Spielers und den Score an der Stelle des Kommers. 
        scores.append((name, int(score)))      #Die Daten werden als Tupel (name, score) in einer Liste scores gespeichert

    # Die Scores nach der Punktzahl in absteigender Reihenfolge sortieren
    sortierte_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Die Top 10 Scores zurückgeben (oder weniger, wenn weniger als 10 Einträge vorhanden sind)
    return sortierte_scores[:10]

# Beispielaufruf:
# Einen neuen Score hinzufügen
score_hinzufuegen('Alice', 250)
score_hinzufuegen('Bob', 300)
score_hinzufuegen('Charlie', 150)

# Die besten 10 Scores holen
top_scores = beste_scores()
print("Top 10 Scores:")
for i, (name, score) in enumerate(top_scores, 1): #i stellt die Platzierungen dar (beginnend bei 1) und enumerate loopt über die Tuples in der Liste der besten Scores.
    print(f"{i}. {name}: {score}") # Gibt <= obersten 10 Tuple Päärchen wieder