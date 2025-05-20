#Aggressive cows
'''We need to return the maximum of all min distances while placing the cows in the stalls'''
#check if the given min dist is possible or not
a=[1,2,5,7,10]
c=3
k=5
prev=a[0]
count=1
for i in range(1,len(a)):
    if a[i]-prev>=k:
        count+=1
        prev=a[i]
    if count==c:
        break
if c==count:
    print('Yes')
else:
    print('No')

#-->brute force approach
a=[1,2,5,7,10]
k=1
while(1):
    c=3
    prev=a[0]
    c-=1
    for i in range(1,len(a)):
        if a[i]-prev>=k:
            c-=1
            prev=a[i]
    if c<=0:
        k+=1
        
    else:
        break
print(k-1)

#Binary search
a=[1,2,5,7,10]
a.sort()
l=0
r=a[-1]-a[0]
res=0
while l<=r:
    c=3
    m=(l+r)//2
    prev=a[0]
    c-=1
    for i in range(1,len(a)):
        if a[i]-prev>=m:
            c-=1
            prev=a[i]
        if c==0:
            break
    if c<=0:
        res=m
        l=m+1
    else:
        r=m-1
print(res)

#using functions
def min_count(a,c,k):
    prev=a[0]       
    for i in range(1,len(a)):
        if a[i]-prev>=k:
            c-=1
        if c<=0:
            return True
    return False
    
def aggressiveCows(a,c):
    l=0
    r=a[-1]-a[0]
    res=0
    m=(l+r)//2
    if min_count(a,c,m):
        res=m
        l=m+1
    else:
        r=m-1
    return res
a=[1,2,5,7,10]
c=3
print(aggressiveCows(a,c))


    
            
    
            


    
            
    
            
        
