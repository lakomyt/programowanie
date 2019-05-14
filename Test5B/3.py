def SortPoly(P,n):
	unsorted = True
	while unsorted:
		unsorted = False
		for x in range(0,n-1):
			if (P[x][0]*P[x][1])>(P[x+1][0]*P[x+1][1]):
				unsorted = True
				q = P[x+1]
				P[x+1] = P[x]
				P[x] = q
