n = int(input())
max = -1

while n > 0:
    x = n % 10
    n = n // 10
    if x > max:
        max = x
print(max)
