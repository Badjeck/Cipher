def caesar_encryption(message):
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

def interval_decryption(message):
    '''
    Déchiffrement par décalage d'un message
    '''
    listMessage = list(message.upper())
    newListMessage = []
    for interval in range(1, len(message)) :
        del newListMessage[:]
        for char in listMessage :
            if char == ' ' :
                newListMessage.append(' ')
            else :
                if ord(char) + interval <= 90 :
                    newListMessage.append(chr(ord(char) + interval))
                else :
                    newListMessage.append(chr(ord(char) + interval - 26))
        interval = "%02d" % interval
        print(f"{interval}  {''.join(newListMessage)}")