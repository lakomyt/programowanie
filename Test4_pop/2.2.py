# Algorytm wypisuje liczby, które pojawiają się w tablicy tylko raz

T = [2,3,4,2,4,1]
T = [2,3,3,3,3,3]
n = len(T)
x=0 #*

for i in range(0,n):
	c = 0
	for j in range(0,n):
		if T[i]!=T[j]:
			c+=1
			x+=1
	if n-c-1==0:
		print('T[i]: ',T[i])
