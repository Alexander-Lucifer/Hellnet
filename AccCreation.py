import Frame as Fr
import Login as l
import os
import consolemenu
import pandas as pd
def Accounts():
    while True:
        os.system('clear')
        print("\n")
        print("\n")
        print("\n Example Mail address \n Demon123@hell.com \n")
        print("\n")
        Name = input("Enter your Name:- ")
        print("\n")
        
        Num = (input("Enter Phone No.:- "))
        if (len(Num) < 10) and (len(Num) > 10):
            raise ValueError("invalid Number, Try again later...")

        print("\n")
        Mail = input("Enter Custom Mail Address(ending with hell.com):- ")

        if Mail.endswith("@hell.com") == False:
            raise ValueError("Invalid Id, Try again later...")
        print("\n")
        Pass = input("PassWord:- ")
        print("\n")
        Conf = input("Confirm PassWord:- ")
        print("\n")

        if Pass != Conf:
            raise ValueError("Passwords don\'t match")
        


        listChr = ["@", "hell.com"]


 

        Acc = open("Acc.csv", 'r')
        Cont = Acc.read()
        if (Num in Cont) and (Mail in Cont):
            print("An Error Occurred \n Account Already Exists for This Phone NUmber and Email ID", '\n')
            Acc.close()
        else:
            Acc = open("Acc.csv", 'a')
            Acc.write(Name),Acc.write(","), Acc.write(Num),Acc.write(","), Acc.write(Mail),Acc.write(","), Acc.write(Pass)
            Acc.close()
    
        print("Press 1 to Go back \nPress 2 to Login")

        Z = int(input())

        if Z == 1:
            Fr.Frame()
        elif Z == 2:
            l.Accounts()
        elif Z == 3:
            df = pd.read_csv("acc.csv")
            print(df)
            
            
            
            
        