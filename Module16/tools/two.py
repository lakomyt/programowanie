from tools.one import Rows

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
