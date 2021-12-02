
def mediap(vet,n):
    s   = 0
    cp  = 0
    pos = 0

    while pos < n:
        if vet[pos]%2==0:
            cp=cp+1
            s=s+vet[pos]

            pos=pos+1
        else:
            pos=pos+1

    return(s/cp)

list = mediap([2,6,5],3)

print(list)