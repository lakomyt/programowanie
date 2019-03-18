def Mode(T,n):
    c=0
    dominanta=T[c]
    oldi=1
    while c<=n:
        y=T[c]
        i=0
        while T[c]==y:
            i+=1
            c+=1
        if oldi<i:
            oldi=i
            dominanta=T[c-1]
            continue
        if oldi==i:
            dominanta='nil'
    return dominanta

