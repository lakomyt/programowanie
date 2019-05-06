# Algorytm wypisuje największą liczbę w tablicy

T = [1,3,2,6,4,5]
T = [500,200,180,280,100]
n = len(T)
x=0 #*

for i in range(0,n):
	c = True
	for j in range(0,n):
		if T[i] < T[j]:
			c = False
			x+=1
	if c==True:
		print('Największa liczba to ',T[i])
		break
