n = int(input())
suma = 0

while n > 10:
    x = n % 10
    n = n // 10
    suma += x
suma += n
print(suma)
