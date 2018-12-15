n = int(input())
min = 10

while n > 0:
    x = n % 10
    n = n // 10
    if x < min:
        min = x
print(min)
