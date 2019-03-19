def InsertionSort(T,n):
    for i in range(3,n):
        k = T[i]
        j = i-1
        while j > 1 and T[j] > k:
            T[j+1] = T[j]
            j = j-1
        T[j+1] = k
