def CountPositive(T,n):
	a = 0
	for x in range(0,n):
		if T[x]>0:
			x+=1
	return a

def LongestSeries(T,n):
	max = 0
	len = 0
	for x in range(0,n):
		if T[x]>0:
			len+=1
		else:
			if len>max:
				max = len
			len = 0
	return max
