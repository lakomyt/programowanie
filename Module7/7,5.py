a = 1
ad = 1
T = [0, 0, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 9]
n = len(T) - 1

while n != -1:
    if T[n] == T[n-1]:
        ad = ad+1
        n = n-1
        continue
    else:
        if ad > a:
            a = ad
            d = T[n]
            n = n-1
        else:
            if ad == a:
                d = 'brak'
                n = n-1
            else:
                n = n-1
        ad = 1
print(d)
