#!/usr/bin/python3

import os
import time
import string
import curses.ascii
from bibliocipher import *

listMethods = [
    "Chiffre de César",
    "Chiffrement par substitution",
    "Chiffre de Vigenère"]


def leave_software():
    """
    Cette fonction affiche un message de fin quand l'utilisateur quitte le programme
    """
    print("\tMerci d'avoir utilisé Cipher\n\n\t\t\t\t\tYann LE COZ")
    time.sleep(4)
    os.system("clear")


def show_error(keyboard, checkSubstitutionAlphabet=False, duplicate=False):
    """
    Cette fonction affiche un message d'erreur quand l'utilisateur entre des caractères incorrectes
    """
    print("----------------------------------------------------")
    print("                       ERREUR")
    print("----------------------------------------------------")
    if checkSubstitutionAlphabet:
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
    Cette fonction permet de retourner au menu principal ou de quitter le programme
    """
    answerKeyboard = ''
    while answerKeyboard.upper() != 'O' and answerKeyboard.upper() != 'N':
        if answerKeyboard != '':
            os.system("clear")
            show_error(answerKeyboard)
        print("----------------------------------------------------")
        answerKeyboard = input(
            "\nVoulez-vous retourner au menu principal ? (O/N)\n")
        if answerKeyboard.upper() == 'O':
            os.system("clear")
            print("----------------------------------------------------")
            print("                     MENU PRINCIPAL")
            print("----------------------------------------------------")
            execute_cipher()
        elif answerKeyboard.upper() == 'N':
            print("\n")
            leave_software()


def execute_cipher():
    """
    Cette fonction est le coeur de Cipher, c'est à partir de celle-ci que l'utilisateur peut chiffrer ses messages
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
        print("----------------------------------------------------")
        choiceOfCipherMethod = input("\nEntrez l'index d'une de ces options: ")
    os.system("clear")
    if choiceOfCipherMethod == '1':
        print("----------------------------------------------------")
        print("                 CHIFFRE DE CÉSAR")
        print("----------------------------------------------------")
        message = input("Entrez votre message: ")
        interval = int(input("Entrez la valeur du décalage: "))
        caesar_cipher(message, interval)
        do_you_want_to_continue()
    elif choiceOfCipherMethod == '2':
        print("----------------------------------------------------")
        print("             CHIFFREMENT PAR SUBSTITUTION")
        print("----------------------------------------------------")
        message = input("Entrez votre message: ")
        key = []
        print("\nCONFIGURATION DE L'ALPHABET DE SUBSTITUTION")
        for letterAlphabet in string.ascii_uppercase:
            letterUser = str(input(f"\t{letterAlphabet}: "))
            while len(letterUser) != 1 or letterUser.upper() in key or letterUser.isnumeric(
            ) or letterUser.upper() == ' ' or curses.ascii.ispunct(letterUser):
                print("\n")
                if letterUser.upper() in key:
                    show_error(
                        letterUser,
                        checkSubstitutionAlphabet=True,
                        duplicate=True)
                else:
                    show_error(letterUser, checkSubstitutionAlphabet=True)
                letterUser = str(input(f"\t{letterAlphabet}: "))
            key.append(letterUser.upper())
        substitution_cipher(message, key)
        do_you_want_to_continue()
    elif choiceOfCipherMethod == '3':
        print("----------------------------------------------------")
        print("                 CHIFFRE DE VIGENÈRE")
        print("----------------------------------------------------")
        message = input("Entrez votre message: ")
        key = input("Entrez votre clé de chiffrement: ")
        vigenere_cipher(message, key)
        do_you_want_to_continue()
    elif choiceOfCipherMethod.upper() == 'C':
        print("----------------------------------------------------")
        print("                      CRÉDITS")
        print("----------------------------------------------------")
        print("VERSION:                                      v1.0.2\n")
        print("AUTEUR:                                  Yann LE COZ")
        print("ÉTABLISSEMENT:                  Bordeaux Ynov Campus")
        do_you_want_to_continue()
    elif choiceOfCipherMethod.upper() == 'Q':
        leave_software()


os.system("clear")
print("----------------------------------------------------")
print("                 BIENVENUE DANS CIPHER")
print("----------------------------------------------------")
print("Cette application crypte des messages en fonction de\ndifférentes méthodes de chiffrement.\n")
execute_cipher()
