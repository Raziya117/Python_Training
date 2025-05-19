#find the number with freq >len(list)/2
a=[2,1,1,2,3,1,1]
d={}
for i in a:
    d[i]=d.get(i,0)+1
for i in d:
    if d[i]>len(a)/2:
        res=i
print(res)

#OR-->Boyer moore voting algorithm
r=0
c=0
for i in a:
    r=i
    if i==r:
        c+=1
    else:
        c-=1
print(r)

#OR
a=[2,1,1,2,3,1,1]
c=1
res=a[0]
for i in range(1,len(a)):
    if res==a[i]:
        c+=1
    else:
        c-=1
        if c==0:
            res=a[i]
            c=1
print(res)





    

