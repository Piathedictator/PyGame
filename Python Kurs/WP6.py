#WP6
#6.1

#Als erstes muss überprüft werden, ob die Verktoren die gleiche Länge besitzen, da das Skalarprodukt nur für Vektoren gleiche Länge definiert ist

#Beispiel

a = [2, 6, -5]
b = [3, -2, -4]
skalar_produkt = 0

if len(a) != len(b) :
    print("Die Vektoren müssen die gleiche Länge haben. Probier's nochmal.")
else:
    print("Die Vektoren haben die gleiche Länge. Das Skalarprodukt kann berechnet werden")
    for i in range(len(a)):
        skalar_produkt += a[i] * b[i]

    print(f"Das Skalarprodukt ist: {skalar_produkt}")


#6.2
# Eingabe vom Benutzer als Ganzzahl. 

number = input("Gib eine Zahl ein: ")

print(number)

# Jede Ziffer in eine Liste von Integer-Werten umwandeln
digit_list = [int(digit) for digit in number]

# Ergebnis ausgeben
print("Liste der Ziffern:", digit_list)
print(sum(digit_list))
sum_of_digits = 0

for i in digit_list:
    sum_of_digits += i

print(f"Die Summe der Ziffern beträgt {sum_of_digits}.")