n = int(input())
am = 0
c = 2

while c < n:
    if n % c == 0:
        am += 1
    c += 1

if am == 2:
    print('tak')
else:
    print('nie')
