from clear import clear
import pandas as pd
import Global

def searchEngine(n):
    clear()
    print(f'''
        Welcome {n},
        Please Select an Option:-
        *******************
        1) Create your Profile
        2) Search the Database
        *******************''')
    Op = int(input(">_"))
    
    if Op == 1:
        print('Test 1 : Pass')
    elif Op == 2:
        print('Test 2 : Pass')

        


def Accounts():
    while True:
        clear()
        Mail = input("Enter Your Hell.com Address:- ").lower()
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
        
        G = None

        
        Auth : bool

        for i in range(l):
            n = nM[i]
            p = pN[i] # PhnNum
            m = Ml[i] # Mail
            pss = ps[i] # Pass
            
            
            
        
            
            if (m == Mail) and (pss == int(Pass)):
                print(f'User {n}, Access Authorized')
                G = n
                Auth = True
                break
            else:
                
                Auth = False
                continue
            
            
        if Auth == True:
            searchEngine(G)
        elif Auth == False:
            print("Error 404, Account not Found")
        
        
        O = input()
        
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
