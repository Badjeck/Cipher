def caesar_encryption(message):
    '''
    Chiffre le message entré par l'utilisateur en utilisant le code César
    '''
    print(f"Votre message:\n{message.upper()}")
    # Convertion du message mise en majuscule en Liste
    listMessage = list(message.upper())
    # Définition du tableau qui va contenir les caractères encodés
    newListMessage = []
    # Demande à l'utilisateur d'entrer une valeur de décalage
    interval = int(input("Entrez la valeur du décalage: "))
    # Pour chaque caractère dans la liste listMessage, on calcule un nouveau caractère qui sera égal à la valeur de ASCII du caractère dans le tableau  - le code ASCII 64 + le décalage indiqué par l'utilisateur
    for char in listMessage :
        newChar = ord(char) - 64 + interval
        if newChar > 26 :
            rest = newChar - 26
        else :
            rest = newChar
        # On ajoute la valeur du caractère encodé dans le tableau newListMessage
        newListMessage.append(chr(rest + 64))
    # On affiche la valeur des caractères encodés concaténée en un seul mot
    print(f"Votre message crypté:\n{''.join(newListMessage)}")



