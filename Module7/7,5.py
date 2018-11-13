a = 1
ad = 1
T = [1,2,3,4,5,6,6,6,7,7,8,9,9]
n = len(T) - 1

while n != -1:
    if T[n] == T[n-1]:
        ad = ad+1
        n = n-1
        if a == 0:
            d = T[n]
        continue
    else:
        if ad > a:
            a = ad
            d = T[n]
        else:
            if ad == a:
                d = 'brak'
        n = n-1
        ad = 1
print(d)
