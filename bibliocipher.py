import string


def caesar_cipher(message, interval):
    '''
    Chiffre le message entré par l'utilisateur en utilisant le chiffre de César
    '''
    listCipher = ""
    for char in message.upper():
        newChar = ord(char) - 64 + interval
        if newChar > 26:
            rest = newChar - 26
        else:
            rest = newChar
        listCipher += chr(rest + 64)
    print(f"\nVotre message chiffré est:\n{listCipher}")


def substitution_cipher(message, key):
    '''
    Chiffre le message entré par l'utilisateur en utilisant la méthode de substitution
    '''
    alphabet = string.ascii_uppercase
    cipherMessage = ""
    for letter in message.upper():
        search = alphabet.find(letter)
        if search < 0:
            cipherMessage += letter
        else:
            cipherMessage += key[search]
    print(f"\nVotre clé de chiffrement est:\n{' '.join(key)}")
    print(f"Votre message chiffré est:\n{cipherMessage}")


def vigenere_cipher(message, key):
    """
    Chiffre le message entré par l'utilisateur en utilisant le chiffre de Vigenère
    """
    alphabet = string.ascii_uppercase
    cipherMessage = ""
    for counter, letter in enumerate(message.upper()):
        search = alphabet.find(letter.upper())
        if search < 0:
            cipherMessage += letter.upper()
        else:
            cipherLetter = ord(key.upper()[counter % len(key.upper())])
            cipherMessage += chr((ord(letter.upper()) + cipherLetter) % 26 + 65)
    print(f"\nVotre message chiffré est:\n{cipherMessage}")