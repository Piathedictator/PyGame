#WP8
#8.1 Fibonacci Series
print("Rekursiver Ansatz: ")
def fibonacci(n):
    if n == 0:
        return 0        #Basisfall
    elif n == 1:
        return 1        #Basisfall
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)      #Rekursiver Fall


for i in range(8):
    print(f"Fibonacci({i}) = ", fibonacci(i))

print(" ")
print("Iterierender Ansatz: ")

def fibonacci2(n):
    if n > 1:
        return fibonacci2(n - 1) + fibonacci2(n - 2)      
    elif n == 1:
        return 1
    elif n == 0:
        return 0

for i in range(8):
    print(f"Fibonacci({i}) = ", fibonacci2(i))

#8.2 Integral
#1
import math

def integrate(f, a, b, N):
    # Schritt 1: Breite von jedem Rechteck berechnen
    width = (b - a) / N  #Integrationsinterval in N gleich große Rechtecke aufteilen, "a" ist der Startpunkt des Intervalls und "b" das Ende
    total_area = 0.0

    # Schritt 2: Rechtecke für jedes Intervall berechnen und summieren
    for i in range(N):
        # Mittelpunkt des Intervalls berechnen
        x_mid = a + (i + 0.5) * width
        # Fläche des Rechtecks hinzufügen
        total_area += f(x_mid) * width

    return total_area

# Testfälle
print(integrate(math.sin, 0, math.pi, 10000))  # Erwartetes Ergebnis: ungefähr 2
print(integrate(math.sin, 0, 2 * math.pi, 10000))  # Erwartetes Ergebnis: ungefähr 0


#2
def antiderivative(f, N=10000):
    # Rückgabefunktion, die das Integral von 0 bis x approximiert (unbestimmtes Integral)
    def F(x):
        return integrate(f, 0, x, N)
    
    return F

# Antiderivative der Sinusfunktion berechnen
F = antiderivative(math.sin)

# Beispielwerte testen
print(F(math.pi))  # Erwartetes Ergebnis: ungefähr 2.0
print(F(2 * math.pi))  # Erwartetes Ergebnis: ungefähr 0.0