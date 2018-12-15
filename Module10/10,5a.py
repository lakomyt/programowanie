n = int(input())    ## 1 <= k <= n
k = int(input()) - 1

for x in range(k):
    n = n * (n+x)

print(n)