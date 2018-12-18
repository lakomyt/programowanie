n = int(input())
am = 0
c = 2

while n > 1:
    if n % c == 0:
        am += 1
        n = n // c
    else:
        c += 1

if am == 2:
    print('tak')
else:
    print('nie')
