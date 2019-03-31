from tools import Display

def Draw(n):
    for x in range(0,n):
        q = n-x-1
        for z in range(0,n):
            if z<=q:
                T[x][z]=0
            else:
                T[x][z]=1
    return T
