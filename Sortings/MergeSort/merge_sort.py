def merge_sort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=merge_sort(a[:mid])
    right=merge_sort(a[mid:])
    return merge(left,right)
    
def merge(l,r):
    i,j=0,0
    c=[]
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            c.append(l[i])#c[k]=l[i] k+=1
            i+=1
        else:
            c.append(r[j])
            j+=1
    while i<len(l):
        c.append(l[i])
        i+=1
    while j<len(r):
        c.append(r[j])
        j+=1
        
    return c
a=[12,4,8,9,2,0,6,5]
m=merge_sort(a)
print(m)