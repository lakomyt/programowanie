#obliczanie reszty z dzielenia
k = input('Podaj dzielną\n')
l = input('Podaj dzielnik\n')
k = int(k)
l = int(l)
x = k
while True:
	if k >= l:
		k = k-l
		continue
	else:
		print("\nReszta z dzielenia %s/%s wynosi %s" % (x,l,k))
		break