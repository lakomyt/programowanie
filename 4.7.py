n = int(input())
k = int(input())
w = 0
g = 1
while w != k:
    b = (n + w)
    w += 1
    g = g * b
print(g)
