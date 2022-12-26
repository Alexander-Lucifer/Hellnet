import AccCreation
import Login 
import adminLogin as aL
import search
import cmd

while True:

    
    '''This Code is Written and Owned By Alexander Lucifer And Suryanshu Mittal
(C)AbyssTech 2022
I do not remember what does what so if you break it you fix it'''

    print('''**********************
Hello!
Welcome To HellNet Ver.0.1
The Official browser for the underworld
(C)AbyssTech
**********************

Disclaimer!
The Current Version Only Supports Text Based Questions

''')



    print("\n")
    print("\n")
    print("\n")
    print('''**********************
Press 1 to create a New HellNet Account
Press 2 if You are an existing user
press 3 for Guest Mode
press 4 for Admin Login
**********************
''')

    N = int(input(">_ "))

    if (N not in range(5)) and (N != 0):
        print("The Option does not Exist, Please choose a valid choice...")
        continue

    if N == 1:
        AccCreation.Accounts()
    elif N == 2:
        Login.Accounts()
    elif N == 4:
        aL.Admin()
    
    elif N == 3:
        search.searchEngine()
