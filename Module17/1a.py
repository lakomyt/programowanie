from tools import Display

def Rectangle(T,a,b,c,d):
    if a>c:
        q = a
        a = c
        c = q
    if b>d:
        q = b
        b = d
        d = q
    for w in range(b,d+1):
        T[a][w] = 1
        T[c][w] = 1
    for w in range(a,c+1):
        T[w][b] = 1
        T[w][d] = 1
