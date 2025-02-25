#WP14
#14.1
import math

def pi(N):
    s = 0  # Startwert für die Summe
    for n in range(1, N + 1):
        s += 1 / (n ** 2)  # Hinzufügen des aktuellen Summanden
        yield math.sqrt(s * 6)  # Berechnung der Pi-Approximation
        
# Ausgabe der Zwischenergebnisse für jeden Summanden
for n, s in enumerate(pi(1000), start=1):
    print(f"Pi approximated by {n:3} summands: {s:.10e}")

#14.2
import random

def kann_dreieck_bilden(a, b, c):
    """Prüft, ob drei Segmente ein Dreieck bilden können."""
    return a + b > c and a + c > b and b + c > a

def simuliere_dreieck_wahrscheinlichkeit(N):
    """Simuliert die Wahrscheinlichkeit, dass aus drei Segmenten ein Dreieck entsteht."""
    erfolg = 0  # Zähler für erfolgreiche Fälle

    for _ in range(N):
        # Zufällige Bruchstellen
        x, y = sorted([random.uniform(0, 1), random.uniform(0, 1)])
        a = x       # Erstes Segment
        b = y - a   # Zweites Segment
        c = 1 - y   # Drittes Segment

        # Prüfen, ob ein Dreieck gebildet werden kann
        if kann_dreieck_bilden(a, b, c):
            erfolg += 1

    # Wahrscheinlichkeit berechnen
    return erfolg / N

# Simulation mit einer großen Anzahl an Versuchen
N = 10000
wahrscheinlichkeit = simuliere_dreieck_wahrscheinlichkeit(N)
print(f"Geschätzte Wahrscheinlichkeit: {wahrscheinlichkeit:.4f}")
