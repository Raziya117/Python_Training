'''Merge two sorted list
[2,4,5,8,9]
[3,5,6,9,11,12,13]'''

def merge(a,b):
    i,j=0,0
    c=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
#     c.extend(a[i:])
#     c.extend(b[j:])
    while j<len(b):
        c.append(b[j])
        j+=1
    while i<len(a):
        c.append(a[i])
        i+=1    
    print(c)
             
a=[2,4,5,8,9]
b=[3,5,6,9,11,12,13]
merge(a,b)

#or
l1=[2,4,5,8,9]
l2=[3,5,6,9,11,12,13]
i=0
j=0
a=[]
for _ in range(len(l1) + len(l2)):
    if i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            a.append(l1[i])
            i += 1
        else:
            a.append(l2[j])
            j += 1
    elif i >= len(l1) and j < len(l2):
        a.append(l2[j])
        j += 1
    elif j >= len(l2) and i < len(l1):
        a.append(l1[i])
        i += 1

print(a)

#OR
def merge(c):
    for i in range(len(c)-1):
        f=0
        for j in range(len(c)-i-1):
            if c[j]>c[j+1]:
                c[j],c[j+1]=c[j+1],c[j]
                f=1
        if f==0:
            break
    print(c)
        
a=[2,4,5,8,9]
b=[3,5,6,9,11,12,13]
c=a+b
merge(c)


        