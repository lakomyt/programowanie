n = int(input())
suma = 1

while n > 10:
    x = n % 10
    n = n // 10
    suma = suma * x
suma = suma * n
print(suma)
