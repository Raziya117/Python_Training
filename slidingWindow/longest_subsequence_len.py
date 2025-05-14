#longest subsequence length 
a=[0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
#a=[1,2,2,3,4,5,6,7,8,9]
#GREEDY ALGORITHM 
c=1
m=1
for i in range(len(a)-1):
    if a[i+1]-a[i]==1: #if a[i]+1==a[i+1]:
        c+=1
        m=max(m,c)
    else:
        c=1      
print(m)
 
#OR O(N)
l=[2,3,4,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
count=1
maxcount=1
for i in range(0,len(l)-1):
    if l[i+1]>l[i]: 
        count+=1
        if count>maxcount:
            maxcount=count
    else:
        count=1
print(maxcount)