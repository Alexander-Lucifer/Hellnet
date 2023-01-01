import os
from platform import system

def clear():
    if system() == 'Windows':
        os.system('cls')
    elif system() == 'Linux':
        os.system('clear')