import os
import search
from platform import system
def Accounts():
    while True:
        if system() == 'Windows':
            os.system('cls')
        elif system() == 'Linux':
            os.system('clear')
        print("\n")
        print("\n")
        print("\n")
        Mail = input("Enter Your Hell.com Address:- ")
        print("\n")
        Pass = input("PassWord:- ")
        print("\n")

        Acc = open("Acc.csv", 'r')
        Cont = Acc.read()

        if Mail and Pass in Cont:
            print("Welcome Back User")
            search.searchEngine()
        else:
            print("Error 404, Account not Found")
            continue