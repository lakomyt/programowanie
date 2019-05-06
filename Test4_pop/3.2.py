from round import Round

def MaxDigit(x):
	max = 0
	while Round(x) != x:
		x = x*10
	while x > 0:
		if x%10 > max:
			max = x%10
		x=x//10
	return max
