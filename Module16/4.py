from tools.one import Rows

def Diagonal(T):
    x = Rows(T)
    suma = 0
    for i in range(0,x+1):
        for j in range(0,x+1):
            if j==i:
                suma += T[i][j]
    return suma
