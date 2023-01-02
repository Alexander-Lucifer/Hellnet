def Authenticate(x, y):
    df = pd.read_csv('Acc.csv')
    l = len(df)
    gf = df.to_dict()
    
    
    nM = gf['Name']

    pN = gf['PhnNum']
    Ml = gf['Mail']
    ps = gf['Pass']
        
    G = None
        
    Auth : bool

    for i in range(l):
        n = nM[i]
        p = pN[i] # PhnNum
        m = Ml[i] # Mail
        pss = ps[i] # Pass
            
            
            
        
            
        if (m == x) and (pss == int(y)):
            print(f'User {n}, Access Authorized')
            G = n
            Auth = True
            break
        else:
                
            Auth = False
            continue
            
            
    if Auth == True:
        print(G)
    elif Auth == False:
        print("Error 404, Account not Found")
        
    return G
        