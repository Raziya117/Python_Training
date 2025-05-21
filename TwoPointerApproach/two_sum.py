#TWO SUM
a=[2,7,11,15]
t=22
i=0
j=len(a)-1
while i<j:
    if a[i]+a[j]==t:
        print(i,j)
        break
    elif a[i]+a[j]>t:
        j-=1
    else:
        i+=1

    