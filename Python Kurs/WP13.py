#WP13
#13.1
class Benutzereingabefehler(Exception):
    """Benutzerdefinierte Ausnahme für ungültige Benutzereingaben."""
    def __init__(self, nachricht="Ungültige Eingabe. Gib bitte eine gültige ganze Zahl ein."):
        super().__init__(nachricht)

def ganzeZahlEingeben(aufforderung="Gib bitte eine ganze Zahl ein: "):
    """
    Fordert den Benutzer auf, eine ganze Zahl einzugeben. Löst Benutzereingabefehler bei ungültigen Eingaben aus.

    Args:
        aufforderung (str): Die Nachricht, die dem Benutzer angezeigt wird.

    Returns:
        int: Die gültige ganze Zahl, die der Benutzer eingegeben hat.

    Raises:
        Benutzereingabefehler: Wenn der Benutzer eine ungültige Eingabe macht.
    """
    try:
        return(int(input(aufforderung)))
    except ValueError:
        raise Benutzereingabefehler(f"Ungültige oder böswillige Eingabe erkannt: '{benutzereingabe}'")


#13.2
class Matrix:
    """Eine Klasse zur Darstellung einer mathematischen Matrix."""
    
    def __init__(self, rows, cols, default_value=0):
        """
        Initialisiert eine Matrix mit der gegebenen Anzahl von Zeilen und Spalten.
        
        Args:
            rows (int): Anzahl der Zeilen.
            cols (int): Anzahl der Spalten.
            default_value (optional): Der Standardwert für alle Elemente (Standard: 0).
        """
        if rows <= 0 or cols <= 0:
            raise ValueError("Zeilen und Spalten müssen größer als 0 sein.")
        self.rows = rows
        self.cols = cols
        self.data = [[default_value for _ in range(cols)] for _ in range(rows)] #Erstellt die Datenstruktur, die die Matrix darstellt. Es handelt sich um eine verschachtelte Liste (Liste von Listen), in der jede innere Liste eine Zeile darstellt.
    
    def __str__(self):
        """Konvertiert die Matrix in eine lesbare String-Darstellung."""
        return "\n".join(["\t".join(map(str, row)) for row in self.data]) #Die Methode erzeugt eine zeilenweise Darstellung der Matrix. Jede Zeile der Matrix wird als eine Zeile in einem String dargestellt, und die Elemente der Zeile werden durch Tabulatoren (\t) getrennt. map() sorgt dafür, dass die str Funktion auf jedes Element in der Zeile (row) angewendet.
    
    def __getitem__(self, indices):
        """
        Ermöglicht den Zugriff auf ein Element der Matrix mit dem Subskriptoperator (z. B. matrix[i, j]).
        
        Args:
            indices (tuple): Ein Tupel (i, j), das Zeile und Spalte angibt.
        
        Returns:
            Der Wert an Position (i, j).
        """
        i, j = indices
        if not (0 <= i < self.rows and 0 <= j < self.cols):
            raise IndexError("Index außerhalb des gültigen Bereichs.")
        return self.data[i][j]
    
    def __setitem__(self, indices, value):
        """
        Ermöglicht das Setzen eines Elements der Matrix mit dem Subskriptoperator.
        
        Args:
            indices (tuple): Ein Tupel (i, j), das Zeile und Spalte angibt.
            value: Der Wert, der gesetzt werden soll.
        """
        i, j = indices
        if not (0 <= i < self.rows and 0 <= j < self.cols):
            raise IndexError("Index außerhalb des gültigen Bereichs.")
        self.data[i][j] = value
    
    def __add__(self, other):
        """
        Ermöglicht die Addition zweier Matrizen mit dem `+`-Operator.
        
        Args:
            other (Matrix): Die zweite Matrix, die addiert werden soll.
        
        Returns:
            Matrix: Die resultierende Matrix nach der Addition.
        
        Raises:
            ValueError: Wenn die Matrizen unterschiedliche Größen haben.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrizen müssen dieselbe Größe haben, um sie zu addieren.")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] + other[i, j]
        return result
    
    def size(self):
        """
        Gibt die Größe der Matrix zurück.
        
        Returns:
            tuple: Ein Tupel (Zeilen, Spalten).
        """
        return self.rows, self.cols


matrix1 = Matrix(2, 2, default_value=1)
matrix2 = Matrix(2, 2, default_value=2)

result = matrix1 + matrix2
print(result)
print(matrix1)
print("")

matrix3 = Matrix(3, 4, default_value=1)
print(matrix3)
