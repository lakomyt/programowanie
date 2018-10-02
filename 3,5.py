p = 1
n = int(input('Podaj \"n\":\n'))
print('\n')
while True:
	if n == p:
		print(n)
		break
	else:
		print(p)
		p += 1
		if p == n:
			print(p)
			break
		else:
			continue