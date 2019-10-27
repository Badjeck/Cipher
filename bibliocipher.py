import string

def caesar_cipher(message):
    '''
    Chiffre le message entré par l'utilisateur en utilisant le code César
    '''
    listCipher = []
    interval = int(input("Entrez la valeur du décalage: "))
    for char in message.upper() :
        newChar = ord(char) - 64 + interval
        if newChar > 26 :
            rest = newChar - 26
        else :
            rest = newChar
        listCipher.append(chr(rest + 64))
    print(f"\nVotre message:\n{message.upper()}\nVotre message crypté:\n{''.join(listCipher)}")

def substitution_cipher(message):
    '''
    Chiffre le message entré par l'utilisateur en utilisant la méthode de substitution
    '''
    alphabet = string.ascii_uppercase
    modifiedAlphabet = ['I', 'A', 'N', 'D', 'E', 'V', 'O', 'P', 'Y', 'L', 'C', 'Z', 'B', 'R', 'D', 'X', 'H', 'T', 'F', 'M', 'S', 'G', 'K', 'Q', 'U', 'W']
    cipherMessage = ""
    for letter in message.upper():
        search = alphabet.find(letter)
        if search < 0:
            cipherMessage += letter
        else:
            cipherMessage += modifiedAlphabet[search]
    print(cipherMessage)
