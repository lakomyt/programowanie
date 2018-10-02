#mnożenie liczb
k = int(input('Podaj czynnik\n'))
l = int(input('Podaj kolejny czynnik\n'))
p = k

#if l == 0:
#	print("\nWynik wynosi %s" % l)
#else:
l = l - 1
while l != 0:
	k = k + p
	l = l - 1
print("\nWynik wynosi %s" % k)