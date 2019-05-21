def Rek(n,k):
	if k==0 or n==k:
		return 1
	if 0<k<n:
		return Rek(n-1,k-1)+Rek(n-1,k)
