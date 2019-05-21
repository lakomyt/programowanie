def Rek(k):
	if k==1:
		return 1
	if k>1 and k%2==0:
		return Rek(k//2)+3
	if k>1 and k%2!=0:
		return Rek(k-1)-1
