n = int(input())
sum = 0
c = 1

while c < n:
    if n % c == 0:
        sum += c
    c += 1
if sum == n:
    print('tak')
else:
    print('nie')