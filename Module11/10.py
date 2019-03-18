k = int(input())
l = int(input())
sumk = 0
suml = 0

for c in range(1,k):
    if k % c == 0:
        sumk += c
if sumk == l:
    for c in range(1,l):
        if l % c == 0:
            suml += c
    if suml == k:
        print('tak')
    else:
        print('nie')
else:
    print('nie')