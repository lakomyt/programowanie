def HorRec(T,n,x):
	if T[n]==1:
		return T[1]
	else:
		return HorRec(T,n-1,x)*x+T[n]
