k = int(input())
kk = k
l = int(input())
ll = l

while k != l:
    while k < l:
        k += kk
    while l < k:
        l += ll

print('NWW: ', k)