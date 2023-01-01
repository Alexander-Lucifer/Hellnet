from clear import clear
import pandas as pd
def Admin():                                                                                                                                                                 
    clear()
    print('''**********************
    Greetings Admin,

    Please Select What you want to do Today:-

    Press 1 to view Collected Data''')

    N = int(input())

    if N == 1:
        Cont = pd.read_csv('Acc.csv')
        print(Cont)