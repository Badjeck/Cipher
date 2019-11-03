import string


def caesar_encryption(message, interval):
    '''
    Encrypts the message entered by the user using Caesar cipher.
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


def substitution_encryption(message, key):
    '''
    Encrypts the message entered by the user using the substitution method.
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


def vigenere_encryption(message, key):
    """
    Encrypts the message entered by the user using Vigenère cipher.
    """

    def define_corresponding_letter(letterMessage, letterKey):
        """
        Return the letter corresponding to the letter of the message and the letter of the key.
        >>> define_corresponding_letter('B', 'Z')
        'A'
        """

        def define_position_letter(letter):
            """
            Return the alphabetical position of the letter set as parameter of the function.
            >>> define_position_letter('A')
            0
            >>> define_position_letter('Z')
            25
            """
            return ord(letter) - 65

        if define_position_letter(letterMessage) + \
                define_position_letter(letterKey) > 25:
            return chr(define_position_letter(letterMessage) +
                       define_position_letter(letterKey) - 26 + 65)
        else:
            return chr(define_position_letter(letterMessage) +
                       define_position_letter(letterKey) + 65)

    alphabet = string.ascii_uppercase
    cipherMessage = []
    for counter, letter in enumerate(message.replace(
            "'",
            '').replace(
            ' ',
            '').replace(
                ',',
                '').replace(
                    '.',
            '').upper()):
        cipherMessage.append(
            define_corresponding_letter(
                letter,
                key.upper()[
                    counter % len(
                        key.upper())]))
    for counter, letter in enumerate(message.upper()):
        if letter not in alphabet:
            cipherMessage.insert(counter, letter)
    print(f"\nVotre message chiffré est:\n{''.join(cipherMessage)}")
