#Found an element in matrix where ro and col both are in increasing order
#nlog(m)
a=[[3,4,6,8],[5,7,9,10],[8,12,13,15],[20,23,26,28],[30,36,40,45]]
n=5
m=4
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

#OR--->o(n+m)
def search(a,k,n,m):
    row=0
    col=m-1
    while row<n and col>=0:
        if a[row][col]==k:
            return True
        elif a[row][col]>k:
            col-=1
        else:
            row+=1
    return False
                       
a=[[3,4,6,8],[5,7,9,10],[8,12,13,15],[20,23,26,28],[30,36,40,45]]
n=5
m=4
k=20
if search(a,k,n,m):
    print('found')
else:
    print('not')


