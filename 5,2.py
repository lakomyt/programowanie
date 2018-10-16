n = int(input("Wpisz n:\n"))
m = n
minp = 2
wynik = 1
while wynik != n:
    reszta = m % minp
    if reszta == 0:
        print (minp)
        wynik = wynik*minp
        if wynik == n:
            break
        else:
            m = m // minp
            continue
    else:
        minp+=1
        continue