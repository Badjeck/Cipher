#!/usr/bin/python3

import os
import time
from bibliocipher import *

def leave_software():
    """
    Cette fonction affiche un message de fin quand l'utilisateur quitte le programme
    """
    print("\n\tMerci d'avoir utilisé Cipher\n\n\t\t\t\t\tYann Le Coz")
    time.sleep(4)
    os.system("clear")

def show_error(keyboard):
    """
    Cette fonction affiche un message d'erreur quand l'utilisateur entre des caractères incorrectes
    """
    os.system("clear")
    print("---------------------------------------------------")
    print("                       ERREUR")
    print("---------------------------------------------------")
    print(f"L'option que vous venez d'entrer ({keyboard}) est incorrecte\n")

def do_you_want_to_continue():
    """
    Cette fonction permet de retourner au menu principal ou de quitter le programme
    """
    reponse = ''
    while reponse.upper() != 'O' and reponse.upper() != 'N':
        if reponse != '':
            show_error(reponse)
        print("---------------------------------------------------")
        reponse = input("\nVoulez-vous retourner au menu principal ? (O/N)\n")
        if reponse.upper() == 'O':
            os.system("clear")
            print("---------------------------------------------------")
            print("                  MENU PRINCIPAL")
            print("---------------------------------------------------")
            execute_cipher()
        elif reponse.upper() == 'N':
            leave_software()

def execute_cipher():
    """
    Cette fonction est le coeur de Cipher, c'est à partir de celle-ci que l'utilisateur peut chiffrer ses messages
    """
    choiceOfCipherMethod = ''
    while choiceOfCipherMethod != '1' and choiceOfCipherMethod != '2' and choiceOfCipherMethod.upper() != 'C' and choiceOfCipherMethod.upper() != 'Q':
        if choiceOfCipherMethod != '':
            show_error(choiceOfCipherMethod)
        print("Méthodes de chiffrement disponibles:")
        print("1 - Chiffrement de César")
        print("2 - Chiffrement de substitution")
        print("\nC - Crédits\nQ - Sortir de Cipher")
        print("---------------------------------------------------")
        choiceOfCipherMethod = input("\nEntrez l'index d'une de ces options: ")
    os.system("clear")
    if choiceOfCipherMethod == '1':
        print("---------------------------------------------------")
        print("                 MÉTHODE DE CÉSAR")
        print("---------------------------------------------------")
        caesar_cipher()
        do_you_want_to_continue()
    elif choiceOfCipherMethod == '2':
        print("---------------------------------------------------")
        print("              MÉTHODE DE SUBSTITUTION")
        print("---------------------------------------------------")
        substitution_cipher()
        do_you_want_to_continue()
    elif choiceOfCipherMethod.upper() == 'C':
        print("---------------------------------------------------")
        print("                     CRÉDITS")
        print("---------------------------------------------------")
        print("VERSION:                                     v1.0.1\n")
        print("AUTEUR:                                 Yann Le Coz")
        print("ÉTABLISSEMENT:                 Bordeaux Ynov Campus")
        do_you_want_to_continue()
    elif choiceOfCipherMethod.upper() == 'Q' :
        leave_software()

os.system("clear")
print("---------------------------------------------------")
print("              BIENVENUE DANS CIPHER")
print("---------------------------------------------------")
execute_cipher()