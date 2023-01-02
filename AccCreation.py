import Frame as Fr
import Login as l
import pandas as pd
from clear import clear
def Accounts():
    while True:
        clear()
        print("\n Example Mail address \n Demon123@hell.com \n")
        print("\n")
        Name = input("Enter your Name:- ")
        print("\n")
        
        Num = (input("Enter Phone No.:- "))
        if (len(Num) < 10) or (len(Num) > 10):
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


 

        #Acc = open("Acc.csv", 'r')
        #Cont = Acc.read()
        
        df = pd.read_csv('acc.csv')
        v = len(df)
        gf = df.to_dict()

        pN = gf['PhnNum']
        Ml = gf['Mail']
        ps = gf['Pass']
        
        for i in range(v):
            p = pN[i] # PhnNum
            m = Ml[i] # Mail
            pss = ps[i] # Pass
            if (Num == p) or (Mail == m):
                print("An Error Occurred \n Account Already Exists for This Phone NUmber and Email ID", '\n')
                
            else:
                Acc = open("Acc.csv", 'a')
                Acc.write('\n')
                Acc.write(Name.title()),Acc.write(","), Acc.write(Num),Acc.write(","), Acc.write(Mail.lower()),Acc.write(","), Acc.write(Pass)
                Acc.close()
    
        print("Press 1 to Go back \nPress 2 to Login\nPress 4 to retry")

        Z = int(input())

        if Z == 1:
            Fr.Frame()
        elif Z == 2:
            l.Accounts()
        elif Z == 3:
            df = pd.read_csv("acc.csv")
            print(df)
        elif Z == 4:
            continue