# Algorytm wypisuje liczby, które występują w tablicy parzystą ilość razy

T = [1,3,4,3,2,1]
T = [7,8,2,3,3,3]
n = len(T)
x=0 #*

for i in range(0,n):
	c = 0
	for j in range(0,n):
		if T[i] == T[j]:
			c+=1
			x+=1
	if c % 2 == 0:
		print(T[i])
