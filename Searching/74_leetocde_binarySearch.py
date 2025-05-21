a=[[1,2,3],[4,5,6],[7,8,9]]
k=5
for i in range(len(a)):
    f=0
    for j in range(len(a)):
        if a[i][j]==k:
            print('Found')
            f=1
            break
    if f==1:
        break
else:
    print('Not')
    

#FINDING an element in matrix with a order
#O(logn*m)
def binary(a,k,n,m):
    l=0
    r=(n*m)-1
    while l<=r:
        f=0
        mid=(l+r)//2
        if a[mid//m][mid%m]==k:
            return 1
            break
        elif a[mid//m][mid%m]>k:
            r=mid-1
        else:
            l=mid+1
    return 0

#a=[[2,3,7,8,9],[10,15,20,22],[23,26,35,36,37],[38,39,41,42,43]]
a=[[2,5,8,10],[13,15,17,22],[23,26,28,33]]
n=3
m=4
k=14
if binary(a,k,n,m):
    print('Found')
else:
    print('Not found')

#OR--->o(logm)+o(logn)
a=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
n=4
k=23
def binary(a,k):
    l=0
    r=len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==k:
            return 1
        elif a[m]>k:
            r=m-1
        else:
            l=m+1
    return 0
for i in a:
    f=1
    if i[-1]>=k:
        if (binary(i,k)):
            f=0
            print('Found')
            break
if f==1:
    print('Not found')
    
    
#OR
#n+Log(m)
a=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
n=4
k=23
def binary(a,k):
    l=0
    r=len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==k:
            return 1
        elif a[m]>k:
            r=m-1
        else:
            l=m+1
    return 0
                                
for i in a:
    f=1
    if i[0]<=k and i[-1]>=k:
        if (binary(i,k)):
            f=0
            print('Found')
            break
if f==1:
    print('Not found')

  

    
            
            
        