from rand import Random

def CircleRandom(k,l):
	x = Random(2l+1)+k-l-1
	return x

def RandomWalk(T,n,k):
	if n==0:
		return T
	T = [CircleRandom(0,k)]
	for i in range(1,n):
		y = CircleRandom(T[i-1],k)
		T.append(y)
	return T

def AddOnes(T,n,k):
	for x in range(0,k):
		r = Random(n+1)-1
		for y in range(0,n-r+1):
			w = n-y
			T[w+1]=T[w]
		T[r] = 1
	return T
