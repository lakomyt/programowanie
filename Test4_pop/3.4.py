from rand import Random

def CircleRandom(k,l):
	x = Random(k+l-(k-l)+1)+k-l-1
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
		r = Random(n)
		for y in range(r,n+1):
			w = T[r+1]
			T[r+1] = T[r]
		T[r] = 1
	return T
