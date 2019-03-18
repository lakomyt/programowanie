T = [1,0,3,4,5,0,7,0,9,10]
n = 10
parz = 0

for i in range (0,n):
    d = T[i]
    if d == 0:
        continue
    else:
        w = d % 2
        if w == 0:
            parz+=1
            continue
        else:
            continue

print(parz)
