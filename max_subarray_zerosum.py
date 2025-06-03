#print max subarray with sum 0
a=[-1,2,-1,2,-1,-2,1]
s,m=0,0
d={}
start=-1
for i in range(len(a)):
    s+=a[i]
    if s==0:
        m=i+1
        start=0
    elif s in d:
        m=max(m,i-d[s])
        start=d[s]+1
    else:
        d[s]=i
print(m,a[start:start+m])