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
    while answerKeyboard.upper() != 'O' and answerKeyboard.upper() != 'N':
        if answerKeyboard != '':
            os.system("clear")
            show_error(answerKeyboard)
        print("---------------------------------------------------------------")
        answerKeyboard = input(
            "\nVoulez-vous retourner au menu principal ? (O/N)\n")
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
    This is the general function of Cipher, it is from it that users can encrypt their various messages.
    """
    choiceOfCipherMethod = ''
    while choiceOfCipherMethod != '1' and choiceOfCipherMethod != '2' and choiceOfCipherMethod != '3' and choiceOfCipherMethod.upper(
    ) != 'C' and choiceOfCipherMethod.upper() != 'Q':
        if choiceOfCipherMethod != '':
            os.system("clear")
            show_error(choiceOfCipherMethod)
        print("Méthodes de chiffrement disponibles:")
        for index, nameMethods in enumerate(listMethods, 1):
            print(f"{index} - {nameMethods}")
        print("\nC - Crédits\nQ - Sortir de Cipher")
        print("---------------------------------------------------------------")
        choiceOfCipherMethod = input("\nEntrez l'index d'une de ces options: ")
    if choiceOfCipherMethod.upper() != 'Q':
        os.system("clear")
    if choiceOfCipherMethod == '1':
        print("---------------------------------------------------------------")
        print("                      CHIFFRE DE CÉSAR")
        print("---------------------------------------------------------------")
        message = input("Entrez votre message: ")
        shift = input("Entrez la valeur du décalage: ")
        while shift.isnumeric() == False:
            print("\n")
            show_error(shift, True)
            shift = input("\tVeuillez entrez le nombre de décalage: ")
        caesar_encryption(message, int(shift))
        do_you_want_to_continue()
    elif choiceOfCipherMethod == '2':
        print("---------------------------------------------------------------")
        print("                 CHIFFREMENT PAR SUBSTITUTION")
        print("---------------------------------------------------------------")
        message = input("Entrez votre message: ")
        key = []
        print("\nCONFIGURATION DE L'ALPHABET DE SUBSTITUTION")
        for letterAlphabet in string.ascii_uppercase:
            letterUser = str(input(f"\t{letterAlphabet}: "))
            while len(letterUser) != 1 or letterUser.upper() in key or letterUser.isnumeric(
            ) or letterUser.upper() == ' ' or curses.ascii.ispunct(letterUser):
                print("\n")
                if letterUser.upper() in key:
                    show_error(letterUser, False, True, True)
                else:
                    show_error(letterUser, False, True)
                letterUser = str(input(f"\t{letterAlphabet}: "))
            key.append(unidecode(letterUser).upper())
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
print("Cette application chiffre des messages en fonction de plusieurs\nméthodes de chiffrement synchrone.\n")
cipher_core()
