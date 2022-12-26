import Login 
import adminLogin as aL
import search
def Frame():

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
Press 1 To Login
press 2 To view your Data
**********************
''')

        N = int(input(">_ "))

        if (N not in range(3)) and (N != 0):
            print("The Option does not Exist, Please choose a valid choice...")
            continue

        elif N == 1:
            Login.Accounts()
    
