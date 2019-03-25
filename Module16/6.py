from one import Rows
from two import Columns
T = [[2,3,5,2,7,'nil'],[1,8,9,0,1,'nil'],[2,8,4,2,1,'nil'],[2,-13,12,10,21,'nil'],'nil']

def Min2D(T):
    min = T[0][0]
    x = Rows(T)
    y = Columns(T)
    for i in range(0,x+1):
        for j in range(0,y+1):
            if T[i][j]<min:
                min = T[i][j]
    return min

print(Min2D(T))