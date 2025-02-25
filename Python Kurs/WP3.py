#WP 3
#1
# Jahr festlegen 
year = int(input("Give a year: "))
# Überprüfen, ob das Jahr ein Schaltjahr ist
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#WP3
#2

import math

a = float(input("Give a value: "))
b = float(input("Give a value: "))
c = float(input("Give a value: "))

# Überprüfung der Sonderfälle
if a == 0:
    if b == 0:
        if c == 0:
            print("Unendlich viele Lösungen, da die Gleichung 0 = 0 ist.")
        else:
            print("Keine Lösung, da die Gleichung widersprüchlich ist.")
    else:
        # Lineare Gleichung bx + c = 0 lösen
        x = -c / b
        print(f"Eine Lösung: x = {x}")
else:
    # Diskriminante berechnen
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


