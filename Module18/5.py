def MinRec(T,k,l):
	if k==l:
		return (T[k])
	x = MinRec(T,k,l-1)
	if x>T[l]:
		return T[l]
	return x
