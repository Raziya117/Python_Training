# remove k elements from front or back and removed cards count must be maximum
# constat sliding window
a=[4,2,7,20,8,6,8,1]
k=3
s=0
for i in range(k):
    s+=a[i]
l=k-1
r=len(a)-1
maxi=s
m2=s
for i in range(1,k+1):
    m2-=a[l]
    m2+=a[r]
    maxi=max(maxi,m2)
    l-=1
    r-=1
print(maxi)

# OR
a=[4,2,7,20,8,6,8,1]
k=3
n=len(a)
ls=0
for i in range(k):
    ls+=a[i]
maxi=ls
rs=0
for i in range(k,-1,-1):
    ls-=a[i]
    rs+=a[n-1]
    maxi=max(maxi,ls+rs)
    n-=1
print(maxi)
    
    
    

        
    
    
        
        
    