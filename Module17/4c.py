from tools import Display

def Draw(n):
    T=[]
    for x in range(0,n):
        T.append([])
        q = n-x-1
        v = n+x-1
        for z in range(0,n*2-1):
            if z<=q or z>=v:
                T[x].append('0')
            else:
                T[x].append('1')
    return T
