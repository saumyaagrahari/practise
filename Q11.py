k=1
i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end=" ")
        b+=1
    j=1
    while j<=k:
        print("*  ",end=" ")
        j+=1
    k+=1
    print()
    i+=1
k=4
i=1
while i<=4:
    b=1
    while b<=i:
        print(" ",end=" ")
        b=b+1
    j=1
    while j<=k:
        print("*  ",end=" ")
        j+=1
    k=k-1
    print()
    i=i+1
