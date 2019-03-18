n = int(input())
suma = 0
for i in range(1,n+1):
    silnia = 1
    for x in range(1,i+1):
        silnia *= x
    suma += 1/silnia
print(suma)
