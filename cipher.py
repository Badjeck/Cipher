#!/usr/bin/python3

import os
import time
import curses.ascii
from bibliocipher import *

listMethods = [
    "Chiffre de César",
    "Chiffrement par substitution",
    "Chiffre de Vigenère"]


def leave_software():
    """
    Displays an end message when the user exits the program.
    """
    print("\t\tMerci d'avoir utilisé Cipher\n\n\t\t\t\t\t\t    Yann LE COZ")
    time.sleep(2)
    os.system("clear")


def show_error(
        keyboard,
        isNotNumeric=False,
        checkSubstitutionAlphabet=False,
        duplicate=False):
    """
    Displays an error message when the user enters incorrect characters.
    """
    print("---------------------------------------------------------------")
    print("                             ERREUR")
    print("---------------------------------------------------------------")
    if isNotNumeric:
        print(
            f"Le caractère que vous venez d'entrez ({keyboard}) n'est pas un chiffre.\n")
    elif checkSubstitutionAlphabet:
        if duplicate:
            print(
                f"La lettre que vous venez d'entrer ({keyboard.upper()}) existe déjà.\n\nVeuillez en entrer une nouvelle:")
        else:
            print(
                f"La lettre que vous venez d'entrer ({keyboard}) est incorrecte.\n\nVeuillez entrer de nouveau une lettre de l'alphabet:")
    else:
        print(
            f"L'option que vous venez d'entrer ({keyboard}) est incorrecte.\n")


def do_you_want_to_continue():
    """
    Allows the user to return to the main menu or exit the program.
    """
    answerKeyboard = ''
    print("---------------------------------------------------------------\n")
    while answerKeyboard.upper() != 'O' and answerKeyboard.upper() != 'N':
        if answerKeyboard != '':
            os.system("clear")
            show_error(answerKeyboard)
        answerKeyboard = input(
            "Voulez-vous retourner au menu principal (O/N)? ")
        if answerKeyboard.upper() == 'O':
            os.system("clear")
            print("---------------------------------------------------------------")
            print("                         MENU PRINCIPAL")
            print("---------------------------------------------------------------")
            cipher_core()
        elif answerKeyboard.upper() == 'N':
            print("\n")
            leave_software()


def cipher_core():
    """
    This is the general function of Cipher, it is from it that users can encrypt or decrypt their various messages.
    """

    def display_options_message():
        """
        Allows the user to choose to encrypt or decrypt a message he has in his possession.
        """
        choiceOfOption = ''
        print("---------------------------------------------------------------")
        print("                           OPTIONS")
        print("---------------------------------------------------------------")
        print("1 - Chiffrer un message\n2 - Déchiffrer un message")
        print("---------------------------------------------------------------\n")
        while choiceOfOption != '1' and choiceOfOption != '2':
            choiceOfOption = input("Entrez l'index d'une de ces options: ")
        return choiceOfOption

    def check_key(key, letterOfAlphabet, enteredCharacter):
        """
        Verifies that the encryption key entered by the user has no duplicate characters, no numbers and no special characters.
        """
        while len(enteredCharacter) != 1 or enteredCharacter.upper() in key or enteredCharacter.isnumeric() or enteredCharacter.upper() == ' ' or curses.ascii.ispunct(enteredCharacter):
            print("\n")
            if enteredCharacter.upper() in key:
                show_error(enteredCharacter, False, True, True)
            else:
                show_error(enteredCharacter, False, True)
            enteredCharacter = input(f"\t{letterOfAlphabet}: ")
        else:
            key.append(unidecode(enteredCharacter).upper())

    choiceOfCipherMethod = ''
    message = ''
    while choiceOfCipherMethod != '1' and choiceOfCipherMethod != '2' and choiceOfCipherMethod != '3' and choiceOfCipherMethod.upper(
    ) != 'C' and choiceOfCipherMethod.upper() != 'Q':
        if choiceOfCipherMethod != '':
            os.system("clear")
            show_error(choiceOfCipherMethod)
        print("Méthodes de chiffrement disponibles:")
        for index, nameMethods in enumerate(listMethods, 1):
            print(f"{index} - {nameMethods}")
        print("\nC - Crédits\nQ - Sortir de Cipher\n---------------------------------------------------------------")
        choiceOfCipherMethod = input("\nEntrez l'index d'une de ces options: ")
    if choiceOfCipherMethod.upper() != 'Q':
        os.system("clear")
    if choiceOfCipherMethod == '1':
        choiceOfOption = display_options_message()
        os.system("clear")
        print("---------------------------------------------------------------")
        print("                      CHIFFRE DE CÉSAR")
        print("---------------------------------------------------------------")
        while not message:
            if choiceOfOption == '1':
                message = input("Entrez votre message: ")
            else:
                message = input("Entrez le message chiffré: ")
        offset = input("Entrez la valeur du décalage: ")
        while offset.isnumeric() == False:
            print("\n")
            show_error(offset, True)
            offset = input("\tVeuillez entrer le nombre de décalage: ")
        if choiceOfOption == '1':
            caesar_encryption(message, int(offset))
        else:
            caesar_encryption(message, int(offset), True)
        do_you_want_to_continue()
    elif choiceOfCipherMethod == '2':
        print("---------------------------------------------------------------")
        print("                 CHIFFREMENT PAR SUBSTITUTION")
        print("---------------------------------------------------------------")
        message = input("Entrez votre message: ")
        key = []
        print("\nCONFIGURATION DE L'ALPHABET DE SUBSTITUTION")
        for letterAlphabet in string.ascii_uppercase:
            letterUser = input(f"\t{letterAlphabet}: ")
            check_key(key, letterAlphabet, unidecode(letterUser).upper())
        substitution_encryption(message, key)
        do_you_want_to_continue()
    elif choiceOfCipherMethod == '3':
        print("---------------------------------------------------------------")
        print("                     CHIFFRE DE VIGENÈRE")
        print("---------------------------------------------------------------")
        message = input("Entrez votre message: ")
        key = input("Entrez votre clé de chiffrement: ")
        vigenere_encryption(message, key)
        do_you_want_to_continue()
    elif choiceOfCipherMethod.upper() == 'C':
        print("---------------------------------------------------------------")
        print("                          CRÉDITS")
        print("---------------------------------------------------------------")
        print("VERSION:                                                   v1.0\n")
        print("AUTEUR:                                             Yann LE COZ")
        print("ÉTABLISSEMENT:                             Bordeaux Ynov Campus")
        do_you_want_to_continue()
    elif choiceOfCipherMethod.upper() == 'Q':
        print("\n")
        leave_software()


os.system("clear")
print("---------------------------------------------------------------")
print("                    BIENVENUE DANS CIPHER")
print("---------------------------------------------------------------")
print("Cette application chiffre et déchiffre des messages en fonction\nde plusieurs méthodes de chiffrement synchrone.\n")
cipher_core()
