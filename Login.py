import os

def Accounts():
    os.system('clear')
    print("\n")
    print("\n")
    print("\n")
    Mail = input("Enter Your Hell.com Address:- ")
    print("\n")
    Pass = input("PassWord:- ")
    print("\n")

    Acc = open("Accounts.txt", 'r')
    Cont = Acc.read()

    if Mail and Pass in Cont:
        print("Welcome Back User")