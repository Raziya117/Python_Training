#Element with largest frequency
a=[2,13,4,2,5,8,13,13,9]
d={}
for i in a:
    d[i]=d.get(i,0)+1
m=0
for v in d:
    if d[v]>m:
        m=d[v]
        res=v
print(res)

##Element with kth largest frequency
a=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
k=3
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
m=max(d.values())
b=[0 for i in range(m+1)]
for i in d:
    b[d[i]]=i
print(b)
print(b[-k])
    

    
