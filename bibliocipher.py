import string

def caesar_cipher():
    '''
    Chiffre le message entré par l'utilisateur en utilisant le code César
    '''
    message = input("Entrez votre message: ")
    interval = int(input("Entrez la valeur du décalage: "))
    listCipher = []
    for char in message.upper():
        newChar = ord(char) - 64 + interval
        if newChar > 26:
            rest = newChar - 26
        else:
            rest = newChar
        listCipher.append(chr(rest + 64))
    print(f"\nVotre message chiffré est:\n{''.join(listCipher)}")

def substitution_cipher():
    '''
    Chiffre le message entré par l'utilisateur en utilisant la méthode de substitution
    '''
    message = input("Entrez votre message: ")
    alphabet = string.ascii_uppercase
    modifiedAlphabet = ['I', 'A', 'N', 'D', 'E', 'V', 'O', 'P', 'Y', 'L', 'C', 'Z', 'B', 'R', 'D', 'X', 'H', 'T', 'F', 'M', 'S', 'G', 'K', 'Q', 'U', 'W']
    cipherMessage = ""
    for letter in message.upper():
        search = alphabet.find(letter)
        if search < 0:
            cipherMessage += letter
        else:
            cipherMessage += modifiedAlphabet[search]
    print(f"\nVotre message chiffré est:\n{''.join(cipherMessage)}")
