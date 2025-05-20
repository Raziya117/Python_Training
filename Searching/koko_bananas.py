import math
a=[3,6,7,11]
k=3
h=8
s=0
for i in range(len(a)):
    s=s+(math.ceil(a[i]/k))
    if s>h:
        print('No')
        break
else:
    print('Yes')
    
# if s<=h:
#     print('Yes')
# else:
#     print('No')

#OR
a=[3,6,7,11]
h=8
k=1
while(1):
    s=0
    for i in range(len(a)):
        s=s+(math.ceil(a[i]/k))
        if s>h:
            k+=1

    else:
        print(k)
        break
    

#OR
a=[3,6,7,11]
h=8
k=1
l=1
r=max(a)
res=0
while l<=r:
    s=0
    m=(l+r)//2
    for i in a:
        s=s+math.ceil(i/m)
    if s<=h:
        res=m
        r=m-1
    else:
        l=m+1
print(res)

#OR
a=[3,6,7,11]
h=8
def possibleornot(a,k,h):
    s=0
    for i in a:
        s+=math.ceil(i/k)
    if s<=h:
        return True
    else:
        return False

l=1
r=max(a)
res=0
while l<=r:
    m=(l+r)//2
    if possibleornot(a,m,h):
        res=m
        r=m-1
    else:
        l=m+1
print(res)
    
        
    