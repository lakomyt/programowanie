T = [1,2,3,4,5,6,7]
print(T)
n = len(T) - 1
m = n/2
c = 0
while c<=n:
	a = T[n]
	T[n] = T[c]
	T[c] = a
	c+=1
	n-=1

print(T)
