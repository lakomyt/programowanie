x = int(input("Wpisz x: "))
y = int(input("Wpisz y: "))
z = int(input("Wpisz z: "))
if x>y:
    if x>z:
        if y>z:
            print("Środkowa liczba to ", y)
        else:
            print("Środkowa liczba to ", z)
    else:
        print("Środkowa liczba to ", x)
else:
    if y>z:
        if x>z:
            print("Środkowa liczba to ", x)
        else:
            print("Środkowa liczba to ", z)
    else:
        print("Środkowa liczba to ", y)