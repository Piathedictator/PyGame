def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a given text using Caesar cipher with a given shift.
    
    :param text: str - The input text to encrypt or decrypt.
    :param shift: int - The number of positions to shift (positive for encryption, negative for decryption).
    :return: str - The encrypted or decrypted text.
    """
    result = []
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Normalize the shift to be within 0-25
            normalized_shift = shift % 26
            # Calculate the new character with wrapping around using ASCII values
            new_char = chr((ord(char) - ord('a') + normalized_shift) % 26 + ord('a'))
            result.append(new_char)
        elif char == ' ' or char == '.':  # Spaces and dots remain unchanged
            result.append(char)
        else:
            raise ValueError("Invalid character. Only lowercase letters, spaces, and dots are allowed.")
    
    return ''.join(result)
