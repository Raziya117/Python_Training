#Finding the number if  frequenecy is given
from collections import Counter
def count(ct,k,keys,l,i=0):
    if i==len(keys):
        return l
    if ct[keys[i]]==k:
        l.append(keys[i])
    return count(ct,k,keys,l,i+1)
        
a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=1
ct=Counter(a)
keys=list(ct.keys())
print(count(ct,k,keys,l=[]))

#OR--->dictionary
def value(x,f,d,i=0):
    if i==len(x):
        return 'not found'
    if d[x[i]]==f:
        return x[i]
    return value(x,f,d,i+1)
        
def dic(a,f,d={},i=0):
    if i==len(a):
        return value(list(d.keys()),f,d)
    if a[i] not in d:
        d[a[i]]=1
    else:
        d[a[i]]+=1
    return dic(a,f,d,i+1)

a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
f=3
print(dic(a,f))

#or--->functional recursion
def freq(a,k,i=0):
    if i==len(a):
        return 0
    if a[i]==k:
        return 1+freq(a,k,i+1)
    else:
        return freq(a,k,i+1)

def iterate(a,k,i=0):
    if i==len(a):
        return 'no num found'
    if freq(a,a[i])==k:
        return a[i]
    return iterate(a,k,i+1)
a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=6
print(iterate(a,k))