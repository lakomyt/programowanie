'''n = int(input())
t = []

while n > 0:
    x = n % 2
    t.append(str(x))
    n = n // 2

print(''.join(t))
