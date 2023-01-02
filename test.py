import pandas as pd
import AdminPage as ap
from clear import clear
import Global
'''
f  = int(input("Enter Row:- "))
        
df = pd.read_csv('Admin.csv')
cd = df.to_dict()
#print(cd)
gk = cd['Name']
kg = cd['ID']
jk = cd['Password']
g = gk[f]
k = kg[f]
j = jk[f]
        
if ( k == "supremeone@helladmin.com") and (j == 6669996969):
    print(f"Welcome {g}, Access Granted, Clearance Level = Admin")

df = pd.read_csv('Acc.csv')
l = len(df)
gf = df.to_dict()

pN = gf['PhnNum']
Ml = gf['Mail']
ps = gf['Pass']

print(gf)

for i in range(l):
    p = pN[i] # PhnNum
    m = Ml[i] # Mail
    pss = ps[i] # Pass
    
    #print(p,m,pss)
    
    '''
while True:
    clear()   
    Mail = input("Enter Your Hell.com Address:- ")
    print("\n")
    Pass = input("PassWord:- ")
    print("\n")
    
    
    Global.Authenticate(Mail, Pass)
    
    
    
    
    '''
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
            
        if (m == Mail) and (pss == int(Pass)):
            print(f'User {Global.G} ✅')
        else:
            print('❌')
        
            
        i = input()
    
        
            
        #if (m == Mail) and (pss == int(Pass)):
            #print(f'User {n}')
            
            #M = input("Press Enter\n")'''