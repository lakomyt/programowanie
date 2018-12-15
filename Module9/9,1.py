a = int(input('Wpisz a: '))
b = int(input('Wpisz b: '))

while b != 0:
    c = a % b
    a = b
    b = c

print(a)