#obliczanie wyniku dzielenia całkowitego
k = int(input('Podaj dzielną\n'))
l = int(input('Podaj dzielnik\n'))
p = 0
while True:
	if k<l:
		print ('\nWynik z dzielenia całkowitego wynosi %s' % p)
		break
	else:
		k -= l
		p += 1
		continue