def Longest(T,n):
	max = 0
	for x in range(0,n):
		c = True
		i=0
		Tn=0
		while T[x][Tn+1]!='nil':
			Tn+=1
		while c==True and i<=Tn:
			if T[x][i]=='nil':
				c = False
			i+=1
		if c == True:
			if Tn>max:
				max = Tn+1
		return max

def Swap(T,l,k):
	i = 0
	while T[k][i]!='nil' or T[l][i]!='nil':
		a = T[k][i]
		T[k][i] = T[l][i]
		T[l][i] = a
		i+=1
