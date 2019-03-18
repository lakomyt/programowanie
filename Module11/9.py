n = int(input())
sum = 0

for c in range(1,n):
    if n % c == 0:
        sum += c

if sum == n:
    print('tak')
else:
    print('nie')