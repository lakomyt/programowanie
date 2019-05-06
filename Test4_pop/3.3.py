from rand import Random

def RandomInterval(k,l):
	x = Random(l-k+1)+k-1
	return x

def RandomElement(T,k):
	n = len(T)-1
	x = T[RandomInterval(n-k,n)]
	return x

def RandomPrecision(k,l):
	bf = Random(pow(10,k))-1
	af = Random(pow(10,l))-1
	af = af / pow(10,l)
	x = bf+af
	return x
