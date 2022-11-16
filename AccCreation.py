import Frame as Fr
import os

def Accounts():
    os.system('clear')
    print("\n")
    print("\n")
    print("\n Example Mail address \n Demon123@hell.com \n")
    print("\n")
    Name = input("Enter your Name:- ")
    print("\n")
    Num = (input("Enter Phone No.:- "))
    print("\n")
    Mail = input("Enter Custom Mail Address(ending with hell.com):- ")

    if Mail.endswith("@hell.com") == False:
        raise ValueError
    print("\n")
    Pass = input("PassWord:- ")
    print("\n")
    Conf = input("Confirm PassWord:- ")
    print("\n")

    if Pass != Conf:
        raise ValueError

    if (len(Num) < 10) and (len(Num) > 10):
        raise ValueError

    listChr = ["@", "hell.com"]


 

    Acc = open("Accounts.txt", 'r')
    Cont = Acc.read()
    if (Num in Cont) and (Mail in Cont):
        print("An Error Occurred \n Account Already Exists for This Phone NUmber and Email ID", '\n')
        Acc.close()
    else:
        Acc = open("Accounts.txt", 'a')
        Acc.write(Name),Acc.write("             "), Acc.write(Num),Acc.write("              "), Acc.write(Mail),Acc.write("       "), Acc.write(Pass)
        Acc.write("\n")
        Acc.close()
    
    print("Press 1 to Go back \nPress 2 to Login")

    Z = int(input())

    if Z == 1:
        Fr.Base()
    elif Z == 2:
        Fr.Login()