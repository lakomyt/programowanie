T = [1,2,3,4,5,6,7,8,9,10]
n = 10
parz = 0

for i in range (0,n):
    d = T[i]
    w = d % 2
    if w == 0:
        parz+=1
        continue
    else:
        continue

print(parz)
