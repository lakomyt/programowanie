k = int(input())
aa = 1
ab = 2
c = 2

if k == 1:
    print(aa)

while c != k:
    x = ab
    ab = 2*ab-aa
    aa = c
    c += 1
print(ab)