#assigning the bundles to the approved people.Return the maximum number of assigned people
#o(nlogn)+o(mlogm)+o(n)
p=[1,6,2,3,4,5]
b=[4,2,3,1,1,2]
p.sort()
b.sort()
i,j,c=0,0,0
while i<len(p) and j<len(b):
    if i>len(p):
        break
    if b[j]>=p[i]:
        c+=1
        i+=1
    j+=1
print(c)

#OR
p=[1,6,2,3,4,5]
b=[4,2,3,1,1,2]
b.sort()
c=0
for i in p:
    for j in b:
        if j>=i:
            c+=1
            break
print(c)

#OR
p=[1,6,2,3,4,5]
b=[4,2,3,1,1,2]
m=max(b)
c=0
for i in p:
    if i<=m:
        c+=1
print(c)


        
        