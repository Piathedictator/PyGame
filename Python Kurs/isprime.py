# isprime.py

def is_prime(n):
    """
    Bestimmt, ob eine Zahl n eine Primzahl ist.
    :param n: Integer-Zahl
    :return: True, wenn n eine Primzahl ist, sonst False
    """
    if n <= 1:                  #Zahlen, die kleiner oder gleich 1 sind (z. B. 0, -5), sind keine Primzahlen.
        return False
    if n <= 3:                  #Die Zahlen 2 und 3 sind Primzahlen.
        return True
    if n % 2 == 0 or n % 3 == 0: #Zahlen, die durch 2 oder 3 teilbar sind (außer 2 und 3 selbst), sind keine Primzahlen. Die 4 ist demnach auch keine Primzahl.
        return False
    i = 5
    while i * i <= n: 
        '''
        Die Schleife läuft, solange i * i <= n:
        Wir prüfen nur Teiler bis zur Quadratwurzel von n. Wenn keine Teiler bis √n gefunden werden, ist n prim.
        '''             
        if n % i == 0 or n % (i + 2) == 0:
            return False
        '''
        Prüft, ob n durch i oder i + 2 teilbar ist:
        i repräsentiert Zahlen der Form 6k-1 
        i + 2 repräsentiert Zahlen der Form 6k+1
        Alle Primzahlen außer 2 und 3 liegen in der Form 6k-1 oder 6k+1 vor
        Zahlen wie 6, 12 usw. sind keine Primzahlen, da sie durch 2 oder 3 teilbar sind.
        '''
        i += 6      #Erhöht i um 6, um die nächsten potenziellen Teiler 6k±1 zu prüfen
    return True     #Wenn die Schleife keinen Teiler findet ist n eine Primzzahl

# Diese Nachricht wird nur angezeigt, wenn isprime.py direkt ausgeführt wird.
if __name__ == "__main__":
    print("isprime.py enthält die Funktion is_prime, die prüft, ob eine Zahl prim ist.")
