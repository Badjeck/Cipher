def caesar_cipher(message):
    '''
    Chiffre le message entré par l'utilisateur en utilisant le code César
    '''
    print(f"Votre message:\n{message.upper()}")
    listMessage = list(message.upper())
    newListMessage = []
    interval = int(input("Entrez la valeur du décalage: "))
    for char in listMessage :
        newChar = ord(char) - 64 + interval
        if newChar > 26 :
            rest = newChar - 26
        else :
            rest = newChar
        newListMessage.append(chr(rest + 64))
    print(f"Votre message crypté:\n{''.join(newListMessage)}")

def substitution_cipher(message):
    '''
    Chiffre le message entré par l'utilisateur en utilisant la méthode de substitution
    '''
    listMessage = list(message.upper())
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', "'", ',', '.']
    modifiedAlphabet = ['I', 'A', 'N', 'D', 'E', 'V', 'O', 'P', 'Y', 'L', 'C', 'Z', 'B', 'R', 'D', 'X', 'H', 'T', 'F', 'M', 'S', 'G', 'K', 'Q', 'U', 'W', ' ', "'", ',', '.']
    newListMessage = []
    for letter in listMessage:
        for position, letterAlphabet in enumerate(alphabet):
            if letter == letterAlphabet:
                newListMessage.append(modifiedAlphabet[position])
    print(''.join(newListMessage))
