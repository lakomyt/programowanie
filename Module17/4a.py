from tools import Display

def Draw(n):
    for x in range(0,n):
        for z in range(0,n):
            if z<=x:
                T[x][z]=1
            else:
                T[x][z]=0
    return T
