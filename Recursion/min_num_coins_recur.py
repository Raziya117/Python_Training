# PRINT THE MINIMUM NUM OF COINS TO GET GIVEN SUM IF NOT THEN RETURN -1
def sum_subset2(a,k,l,x,i=0):
    if i==len(a):
        if k==0:
            l.append(x)
        return 
    if a[i]<=k:
        sum_subset2(a,k-a[i],l,x+1,i+1)
    sum_subset2(a,k,l,x,i+1)
k=14
a=[2,4,6,8]
l=[]
sum_subset2(a,k,l,x=0)
if l:
    print(min(l))
else:
    print("-1")
    
    
#OR
def sum_subset(a,k,x=0,i=0,m=999999):
    if i==len(a):
        if k==0:
            if x<m:
                m=x
        return m
    
    if a[i]<=k:
        m=sum_subset(a,k-a[i],x+1,i+1,m)
    m=sum_subset(a,k,x,i+1,m)
    return m
    
a=[2,4,6,8]
k=14
b=sum_subset(a,k)
if b==999999:
    print(-1)
else:
    print(b)

    