#WP15
#15.1
# main.py

from isprime import is_prime
import copy

def main():
    try:
        # Eingabe einer Zahl vom Benutzer
        num = int(input("Geben Sie eine Zahl ein, um zu prüfen, ob sie prim ist: "))
        if is_prime(num):
            print(f"{num} ist eine Primzahl.")
        else:
            print(f"{num} ist keine Primzahl.")
    except ValueError:
        print("Bitte geben Sie eine gültige Ganzzahl ein.")

if __name__ == "__main__":
    main()


#15.2
def bubble_sort(lst2, reverse=False):
    """
    Sortiert die Liste lst mit dem Bubble Sort-Algorithmus.
    
    :param lst: Die Liste, die sortiert werden soll.
    :param reverse: Wenn True, wird die Liste in absteigender Reihenfolge sortiert.
                    Wenn False, wird die Liste in aufsteigender Reihenfolge sortiert.
    :return: Die sortierte Liste.
    """
    lst = copy.deepcopy(lst2)
    n = len(lst)
    
    # Durchlaufe die Liste so oft, bis keine Änderungen mehr notwendig sind
    for i in range(n):
        swapped = False  # Flag, um zu prüfen, ob ein Tausch stattgefunden hat
        
        # Vergleiche benachbarte Elemente und tausche sie bei Bedarf
        for j in range(0, n - i - 1):
            if (lst[j] > lst[j + 1] and not reverse) or (lst[j] < lst[j + 1] and reverse):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Tausche die Elemente
                swapped = True
        
        # Wenn keine Tauschaktionen stattgefunden haben, ist die Liste sortiert
        if not swapped:
            break
    
    return lst

# Beispiele:
lst = [64, 34, 25, 12, 22, 11, 90]
print("Sortiert aufsteigend:", bubble_sort(lst))
print("Sortiert absteigend:", bubble_sort(lst, reverse=True))
