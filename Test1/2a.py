n = int(input("wczytaj liczbe n: "))
a = 1
c = 1
if n == 1:
    print(a)
else:
    while c != n:
        a = 2*a+7
        c += 1
    print(a)    