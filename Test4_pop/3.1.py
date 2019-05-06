from round import Round

def DigitSum(x):
	suma = 0
	while Round(x) != x:
		x = x*10
	while x > 0:
		suma+=x%10
		x=x//10
	return suma
