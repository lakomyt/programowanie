def Rek(k):
	if k==1:
		return 1
	if k>1:
		return Rek(k-1)*2+7
