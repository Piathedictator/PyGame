#16.1



#16.2
def caesar_cipher(text, shift):
    """
    Verschlüsselt oder entschlüsselt einen gegebenen Text mit einer Caesar-Verschlüsselung basierend auf einer bestimmten Verschiebung.
    
    :param text: str - Der zu verschlüsselnde oder zu entschlüsselnde Text.
    :param shift: int - Die Anzahl der Positionen, um die verschoben wird (positiv für Verschlüsselung, negativ für Entschlüsselung).
    :return: str - Der verschlüsselte oder entschlüsselte Text.
    """
    result = []
    
    for char in text:
        if char.isalpha():  # Prüfen, ob der Buchstabe ein gültiger Buchstabe ist
            # Die Verschiebung auf den Bereich 0-25 normalisieren (nur Buchstaben)
            normalized_shift = shift % 26
            # Den neuen Buchstaben berechnen und mit ASCII-Werten arbeiten
            new_char = chr((ord(char) - ord('a') + normalized_shift) % 26 + ord('a'))
            result.append(new_char)
        elif char == ' ' or char == '.':  # Leerzeichen und Punkte bleiben unverändert
            result.append(char)
        else:
            raise ValueError("Ungültiges Zeichen. Nur Kleinbuchstaben, Leerzeichen und Punkte sind erlaubt.")
    
    return ''.join(result)

message = "hallo welt."
shift = 3
encrypted_message = caesar_cipher(message, shift)
print("Verschlüsselt:", encrypted_message)

encrypted_message = "khoor zruog."
shift = -3
decrypted_message = caesar_cipher(encrypted_message, shift)
print("Entschlüsselt:", decrypted_message)

encrypted_message = "pbatenghyngvbaf lbh unir fhpprrqrq va qrpelcgvat gur fgevat."
shift = -13  # Entschlüsseln mit einer Verschiebung von 13

decrypted_message = caesar_cipher(encrypted_message, shift)
print("Entschlüsselte Nachricht:", decrypted_message)

