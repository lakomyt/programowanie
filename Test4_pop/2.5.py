def Round(x):
    if x+0.5 // 1 > x // 1:
        x = x+0.5
    x = x // 1
    return int(x)

def Ceil(x):
    if Round(x)<x:
        x+=1
    x = Round(x)
    return x

def RoundP(x,k):
    q = k
	if k==0:
		return Round(x)
    elif k<0:
        while k!=0:
            x=x*10
            k+=1
        x = Round(x)
        while k!=q:
            x=x/10
            k-=1
    elif k>0:
        while k!=0:
            x=x/10
            k-=1
        x = Round(x)
        while k!=q:
            x=x*10
            k+=1
    return x
