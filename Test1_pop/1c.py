a = int(input())
b = int(input())
c = int(input())

if a > c:
    if a < b:
        print(a)
    else:
        if b > c:
            print(b)
        else:
            print(c)
else:
    if a > b:
        print(a)
    else:
        if b > c:
            print(c)
        else:
            print(b)