def Round(x):
	if x+0.5 // 1 > x // 1:
		x = x+0.5
	x = x // 1
	return int(x)

def Floor(x):
	if Round(x)>x:
		x-=1
	x = Round(x)
	return x

def Digit(x,k):
	if k<0:
		while k!=0:
			x=x*10
			k+=1
	elif k>0:
		while k!=1:
			x=x/10
			k-=1
	x = Floor(x)%10
	return x
