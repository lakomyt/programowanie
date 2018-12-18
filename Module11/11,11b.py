n = int(input())
nn = n
am = 0

while nn > 0:
    nn = nn // 10
    am += 1

z = 1
for x in range(1,am):
    z = z*10

for i in range(1,am+1):
    a = n // z
    print(a)
    n = n - z*a
    z = z // 10
