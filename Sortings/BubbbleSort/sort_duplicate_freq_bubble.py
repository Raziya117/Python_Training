# sorting based on duplicate frequencies
def count(a):
    d={}
    for i in a:
        d[i]=d.get(i,0)+1
    return d

def sorting(d):
    k=list(d.items())
    for i in range(len(k)-1):
        f=0
        for j in range(len(k)-i-1):
            if k[j][0]*k[j][1]>k[j+1][0]*k[j+1][1]:
                k[j],k[j+1]=k[j+1],k[j]
                f=1
        if f==0:
            break
    return k

def re(c):
    res = []
    for num, freq in c:
        res.extend([num] * freq)
    return res
    
a=[7,2,6,3,6,7,7,2,8,8]
b=count(a)
c=sorting(b)
r=re(c)
print(r)