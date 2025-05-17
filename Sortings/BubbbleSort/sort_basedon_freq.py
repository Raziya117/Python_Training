# sort list based on its frequency without duplicates
def count(a):
    d={}
    for i in a:
        d[i]=d.get(i,0)+1
    return d

def sorting(a,d):
    for i in range(len(a)-1):
        f=0
        for j in range(len(a)-i-1):
            if d[a[j]]>d[a[j+1]]:
                a[j],a[j+1]=a[j+1],a[j]
                f=1
        if f==0:
            break
    return a
   
a=[7,2,6,3,6,7,7,2,2,2]
b=count(a)
print(sorting(a,b))