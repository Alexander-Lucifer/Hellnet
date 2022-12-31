Name : str = input("Enter your  Firstname:- ")
if (Name.isalpha()) == False:
    raise ValueError("Name is Invalid")

Nam : str = input("Enter your  Lastname:- ")
if (Nam.isalpha()) == False:
    raise ValueError("Name is Invalid")


Age : int = input("Enter your Age:- ")

phnNUm : int = input("Enter your Number:- ")

Add : str = input("Enter your Address:- ")
if (Add.isalnum()) == False:
    raise ValueError("Name is Invalid")

any : int = input("Enter your Anydesk ID(If you want):- ")

Int : str = input("Enter your intrests W/O comma:- ")

rel : None

print(''' Please tell us your Relationship Status
press Y for Committed/ press N for Single''')
N = input(">_")

if N.lower == 'y':
    rel = "Committed"
elif N.lower == 'n':
    rel = "Single"
else:
    rel = "It's Complicated"
    
a : str = input("Enter Alias:- ")

Acc = open("data.csv", 'a')
Acc.write(Name+" "+Nam),Acc.write(","), Acc.write(Age),Acc.write(","), Acc.write(phnNUm),Acc.write(","), Acc.write(Add), Acc.write(any),Acc.write(","), Acc.write(rel),Acc.write(","), Acc.write(a)
Acc.close()