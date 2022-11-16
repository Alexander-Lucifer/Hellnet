import AdminPage as ap
import os
def Admin():
    print("\n")
    print("\n")
    print("\n")
    Mail = input("Enter Your Helladmin.com Address:- ")
    print("\n")
    Pass = input("PassWord:- ")
    print("\n")

    Adm = open("Admin.txt", 'r')
    Cont = Adm.read()

    if Mail and Pass in Cont:
        ap.Admin()