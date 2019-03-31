from tools import Display

def Draw(n):
    T=[]
    for x in range(0,n*2-1):
        T.append([])
    for x in range(0,n):
        q = n-x-1
        v = n+x-1
        for z in range(0,n*2-1):
            if z<=q or z>=v:
                T[x].append('·')
                if x!=2*n-2-x:
                    T[2*n-2-x].append('·')
            else:
                T[x].append('1')
                if x!=2*n-2-x:
                    T[2*n-2-x].append('1')
    return T
