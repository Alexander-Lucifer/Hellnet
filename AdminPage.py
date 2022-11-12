def Admin():
    print("\n")
    print("\n")
    print("\n")
    print('''**********************
    Greetings Admin,

    Please Select What you want to do Today:-

    Press 1 to view Collected Data''')

    N = int(input())

    if N == 1:
        dt = open("Accounts.txt", 'r')
        Cont = dt.read()
        print(Cont)