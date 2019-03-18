T = [28,11,31,48,52,13,72,65,90,10]
n = 9
min = T[0]
c = 0
while c != n:
    if min>T[c]:
        min=T[c]
        c+=1
    else:
        c+=1

print(min)
