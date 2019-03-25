from one import Rows

def Lower(T):
    x = Rows(T)
    for i in range(0,x+1):
        for j in range(0,i):
            T[i][j]=0
