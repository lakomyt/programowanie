from tools.one import Rows

def Unit(T):
    x = Rows(T)
    for i in range(0,x+1):
        for j in range(0,x+1):
            if j==i:
                T[i][j] = 1
            else:
                T[i][j] = 0
