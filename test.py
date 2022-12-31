import pandas as pd
import AdminPage as ap

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
