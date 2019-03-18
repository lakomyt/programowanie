n = int(input())
t = []
x = 2

while n != 1:
    if n % x == 0:
        t.append(x)
        n = n/x
    else:
        x += 1
        continue
l = len(t)
if l == 2 and t[0] == t[1]:
    print('tak')
else:
    print('nie')
