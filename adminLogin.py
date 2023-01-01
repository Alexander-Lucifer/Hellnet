import AdminPage as ap
from clear import clear
import pandas as pd


def Admin():
    clear()
    c = 3
    while c >= 0:
        clear()
        
        if c == 0:
            print(f'You have {c} mistakes left!')
            #os.abort()
            raise KeyboardInterrupt("Unauthorized Access Attempts!")
        print(f'You have {c} mistakes left!')
        Mail : str = input("Enter Your Helladmin.com Address:- ")
        print("\n")
        Pass  = int(input("PassWord:- "))
        print("\n")
        f  = int(input("Enter Row:- "))
        
        df = pd.read_csv('Admin.csv')
        cd = df.to_dict()
        
        #print(cd)
        gk = cd['Name']
        kg = cd['ID']
        jk = cd['Password']
        
        if f not in range(1):
            c -= 1
            continue
        
        g = gk[f]
        
        k = kg[f]
        j = jk[f]
        
        if ( k == Mail) and (j == Pass):
            print(f"Welcome {gk}, Access Granted, Clearance Level = Admin")
            ap.Admin()
            break
        else:
            c = c-1
            
        

