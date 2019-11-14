import string
from unidecode import unidecode


def define_position_letter(letter):
    """
    Return the alphabetical position of the letter set as parameter of the function.
    >>> define_position_letter('A')
    0
    >>> define_position_letter('Z')
    25
    """
    return ord(letter) - 65


def caesar_encryption(message, offset, decode=False):
    '''
    Encrypts or decrypts the message entered by the user using Caesar cipher.
    >>> caesar_encryption("Caesar", 3)
    "FDHVDU"
    >>> caesar_encryption("FDHVDU", 3, True)
    "CAESAR"
    '''
    cipherMessage = ""
    for letter in unidecode(message).upper():
        if letter not in string.digits and letter not in string.punctuation and letter not in string.whitespace:
            if decode:
                newLetter = define_position_letter(letter) - offset
                if newLetter < 0:
                    newLetter += 26
            else:
                newLetter = define_position_letter(letter) + offset
                if newLetter > 25:
                    newLetter -= 26
            cipherMessage += chr(newLetter + 65)
        else:
            cipherMessage += letter
    print(f"\nVotre message chiffré est:\n{cipherMessage}")


def substitution_encryption(message, key):
    '''
    Encrypts the message entered by the user using the substitution method.
    >>> substitution_encryption("Substitution methode", ['A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N'])
    "LWZLMOMWMOGF DTMIGRT"
    '''
    alphabet = string.ascii_uppercase
    cipherMessage = ""
    for letter in unidecode(message).upper():
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
    >>> vigenere_encryption("J'adore écouter la radio toute la journée", "musique")
    "V'UVWHY IOIMBUL PM LSLYI XAOLM BU NAOJVUY"
    """

    def define_corresponding_letter(letterMessage, letterKey):
        """
        Return the letter corresponding to the letter of the message and the letter of the key.
        >>> define_corresponding_letter('B', 'Z')
        'A'
        """
        if define_position_letter(letterMessage) + \
                define_position_letter(letterKey) > 25:
            return chr(define_position_letter(letterMessage) +
                       define_position_letter(letterKey) - 26 + 65)
        else:
            return chr(define_position_letter(letterMessage) +
                       define_position_letter(letterKey) + 65)

    alphabet = string.ascii_uppercase
    cipherMessage = []
    for counter, letter in enumerate(unidecode(message).replace(
            "'",
            '').replace(
            ' ',
            '').replace(
                ',',
                '').replace(
                    '.',
            '').upper()):
        if letter in alphabet:
            cipherMessage.append(
                define_corresponding_letter(
                    letter,
                    unidecode(key).upper()[
                        counter % len(
                            unidecode(key).upper())]))
    for counter, letter in enumerate(unidecode(message).upper()):
        if letter not in alphabet:
            cipherMessage.insert(counter, letter)
    print(f"\nVotre message chiffré est:\n{''.join(cipherMessage)}")
