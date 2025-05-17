#BUCKET SORT
#sort duplicate frequencies
a=[7,2,6,3,6,7,9,9,9,7,7,2,8,8]
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
for i in d.items():
    b[i[1]].append(i[0])
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)

#OR
def count(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

def bucket_sort(d):
    n=max(d.values())
    b=[]
    for i in range(n+1):
        b.append([])
    for i in d.items():
        b[i[1]].append(i[0])
    return b

def print_list(b):
    c=[]
    for i in range(len(b)):
        for j in b[i]:
            c.extend([j]*i)
    return c

a=[7,2,6,3,6,7,9,9,9,7,7,2,8,8]
l=count(a)
p=bucket_sort(l)
print(print_list(p))