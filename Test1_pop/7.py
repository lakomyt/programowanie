k = int(input())
l = int(input())
sum_k = 0
sum_l = 0
c = 1

while c < k:
    if k % c == 0:
        sum_k += c
    c += 1
if sum_k == l:
    c = 1
    while c < l:
        if l % c == 0:
            sum_l += c
        c += 1
    if sum_l == k:
        print('tak')
    else:
        print('nie')
else:
    print('nie')