def Evaluate(T,n,x):
    suma = 1
    for i in range(0,n+1):
        suma = suma * T[i] * pow(x,n-i)
    return suma
