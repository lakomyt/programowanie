from tools import Display

def Rectangle_f(T,a,b,c,d):
    # P1(a,b)
    # P2(c,d)
    if a>c:
        q = a
        a = c
        c = q
    if b>d:
        q = b
        b = d
        d = q
    for w in range(a,c+1):
        for h in range(b,d+1):
            T[w][h] = 1
