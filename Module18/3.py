def NWD(k,l):
	if l==0:
		return k
	else:
		return NWD(l,k%l)
