# print max subarray count with two unique characters
#we are expanding with same max window size
a=[3,3,3,1,2,1,1,2,3,3,4]
l=0
r=0
d={}
m=0
st=0
for r in range(len(a)):
    if a[r] not in d:
        d[a[r]]=1
    else:
        d[a[r]]+=1
    if len(d)>2:
        d[a[l]]-=1
        if d[a[l]]==0:
            del d[a[l]]
        l+=1
    if r-l+1>m:
        m=r-l+1
        st=l
print(m)
print(a[st:st+m])
        
        
        
        