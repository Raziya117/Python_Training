#Return no of days to ship all weights
def possible(a,c,days):
    d=1
    s=0
    for i in w:
        if s+i>c:
            d+=1
            s=0
        s+=i
    if d<=days:
        return True
    else:
        return False
w=[1,2,3,4,5,6,7,8,9,10]
d=5    
l=max(w)
r=sum(w)
res=0
while l<=r:
    m=(l+r)//2
    if possible(w,m,d):
        res=m
        r=m-1
    else:
        l=m+1
if res:
    print(res)
else:
    print('Not')
     
#Finding the if it is possible in how many days to complete shipping 
#OR
w=[1,2,3,4,5,6,7,8,9,10]
capacity=12
d=1
s=0
for i in w:
    if i>capacity:
        print('Not possible')
        break
    elif s+i<=capacity:
        s+=i
    else:
        d+=1
        s=i
else:
    print(d)
    
    
#OR
w=[1,2,3,4,5,6,7,8,9,10]
capacity=12
d=1
s=0
if capacity<max(w):
    print('Not possible')
else:
    for i in w:
        if s+i<=capacity:
            s+=i
        else:
            d+=1
            s=i
    print(d)
    
    
    