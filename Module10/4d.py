k = int(input())
c = 2
aa = 1
ab = 3

if k == 1:
    print(aa)
    exit()

if k == 2:
    print(ab)
    exit()

while c != k:
    bb = ab
    ab = aa + ab
    aa = bb
    c += 1

print(ab)
