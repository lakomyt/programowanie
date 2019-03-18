'''T = [1,4,5,2,6,3,8,7]
n = len(T) - 1
print(T)
c = 1
while n != -1:
    c = 1
    a = T[n-1]
    b = T[n]
    if a > b:
        T[n-1] = b
        T[n] = a
    else:
        c = c-1
    n = n-1
    if c>0:
        n = len(T) - 1
    continue
print(T)
