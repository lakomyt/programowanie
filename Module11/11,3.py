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

print(t)