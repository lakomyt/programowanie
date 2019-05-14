def CountInterval(T,n,a,b):
	a = 0
	for x in range(0,n):
		if T[x]>=a and T[x]<=b:
			a += 1
	return a

def LongestSeries(T,n,a,b):
	max = 0
	len = 0
	for x in range(0,n):
		if T[x]>=a and T[x]<=b:
			len+=1
		else:
			if len>max:
				max = len
			len = 0
	return max
