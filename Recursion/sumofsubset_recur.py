# If a k value is given checking whether that k is equal to a sum of subset
# OPTIMIZED CODE
def sum_subset(a,k,x=[],i=0):
    if i==len(a):
        if k==0:
            print('True')
            print(x)
        return
    if a[i]<=k:
        sum_subset(a,k-a[i],x+[a[i]],i+1)
    sum_subset(a,k,x,i+1)

a=[2,3,4]
k=5
sum_subset(a,k)

#OR
def sum_subset(a,k,x=[],i=0):
    if i==len(a):
        if sum(x)==k:
            print('True')
        return
    sum_subset(a,k,x+[a[i]],i+1)
    sum_subset(a,k,x,i+1)

a=[2,3,4]
k=5
sum_subset(a,k)

#OR 
def sum_subset(a,k,i=0):
    if k==0:
        return True
    if i==len(a):
        return False
    
    if a[i]<=k:
        return sum_subset(a,k-a[i],i+1) or sum_subset(a,k,i+1)

a=[2,3,4]
k=6
print(sum_subset(a,k))

#OR
def sum_subset(a,k,i):
    if k==0:
        return True
    if i==0:
        return False
    if a[i-1]>k:
        return sum_subset(a,k,i-1)
    return sum_subset(a,k-a[i-1],i-1) or sum_subset(a,k,i-1)

a=[2,3,4]
k=7
print(sum_subset(a,k,len(a)))
    
        