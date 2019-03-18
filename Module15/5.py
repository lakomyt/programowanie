def Counter(T,n):
    for i in range(0,n+1):
        W.append(0)
    for i in range(0,n+1):
        W[T[i]]=W[T[i]]+1
    print(W)
    x = 0
    for i in range(0,n+1):
        if W[i]>0:
            x+=1
    return x
