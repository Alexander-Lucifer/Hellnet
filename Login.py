
from clear import clear
import pandas as pd

def searchEngine():
    clear()
    print('''
            ''')

def Accounts():
    while True:
        clear()
        Mail = input("Enter Your Hell.com Address:- ")
        print("\n")
        Pass = input("PassWord:- ")
        print("\n")
        
        df = pd.read_csv('Acc.csv')
        l = len(df)
        gf = df.to_dict()
        
        
        nM = gf['Name']

        pN = gf['PhnNum']
        Ml = gf['Mail']
        ps = gf['Pass']

        for i in range(l):
            n = nM[i]
            p = pN[i] # PhnNum
            m = Ml[i] # Mail
            pss = ps[i] # Pass
            
            print( '✅', '✅', '✅', '✅')
            
        
            
            if (m == Mail) and (pss == int(Pass)):
                print(f'User {n}')
            #   break
            #  breakpoint(25)
    
    #print(p,m,pss)
        
        '''

        Acc = open("Acc.csv", 'r')
        Cont = Acc.read()

        if Mail and Pass in Cont:
            print("Welcome Back User")
            #searchEngine()
        else:
            print("Error 404, Account not Found")
            continue
Accounts()

'''
