import os
from platform import system
import pandas as pd
def Admin():                                                                                                                                                                 
    if system() == 'Windows':
        os.system('cls')
    elif system() == 'Linux':
        os.system('clear')
    print("\n")
    print("\n")
    print("\n")
    print('''**********************
    Greetings Admin,

    Please Select What you want to do Today:-

    Press 1 to view Collected Data''')

    N = int(input())

    if N == 1:
        Cont = pd.read_csv('Acc.csv')
        print(Cont)