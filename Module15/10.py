def MinI(T,k,n):
    min = T[k]
    p=k
    for i in range(k,n+1):
        if T[i]<min:
            min = T[i]
            p = i
    return p

def zamiana(x,y):
    c = T[x]
    T[x] = T[y]
    T[y] = c

def SortMin(T,n):
    for i in range(0,n+1):
        m = Min(T,i,n)
        zamiana(m,i)


