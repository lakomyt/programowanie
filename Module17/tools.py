
'''
Dodatkowe funkcje ułatwiające operacje na tablicach dwuwymiarowych
'''

def Rows(T):
    x = 0
    i = 1
    while T[i] != 'nil':
        x+=1
        i+=1
    return x

def Columns(T):
    x = Rows(T)
    yy = 1
    for i in range(0,x+1):
        j = 1
        y = 0
        while T[i][j] != 'nil':
            y+=1
            j+=1
        if y>yy:
            yy = y
    return yy

def Display(T):
    D = []
    x = Rows(T)
    y = Columns(T)
    for i in range(0,x+1):
        for j in range(0,y+1):
            D.append(T[i][j])
        print(D)
        D = []