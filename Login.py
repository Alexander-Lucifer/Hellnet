import os
import consolemenu as C
import search
def Accounts():
    while True:
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