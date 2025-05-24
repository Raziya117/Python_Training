a=[1,1,1,0,0,0,1,1,1,1,0]
k=2
l=0
z=0
m=0
for r in range(len(a)):
    if a[r]==0:
        z+=1
    if z>k:
        if a[l]==0:
            z-=1
        l+=1
    if z<=k:
        m=max(m,r-l+1)
print(m)
    
    
#OR

l=0
r=0
c=0
m=1
d={}
while r<len(a):
    if a[r]==0:
        d[c]=r
        c+=1
    if c>k:
        l=d[c-k-1]+1
    m=max(m,r-l+1)
    r+=1
print(m)



    
        
    

    
    
        
    
    