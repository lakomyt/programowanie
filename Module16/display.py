from one import Rows
from two import Columns

'''
Dodatkowa funkcja wyświetlająca tablice dwuwymiarowe w wierszach i kolumnach
'''

def Display(T):
    D = []
    x = Rows(T)
    y = Columns(T)
    for i in range(0,x+1):
        for j in range(0,y+1):
            D.append(T[i][j])
        print(D)
        D = []