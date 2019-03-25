from tools.one import Rows
from tools.two import Columns

def Min2D(T):
    min = T[0][0]
    x = Rows(T)
    y = Columns(T)
    for i in range(0,x+1):
        for j in range(0,y+1):
            if T[i][j]<min:
                min = T[i][j]
    return min
