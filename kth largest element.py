# print the kth largest element
#Considering without duplicates
#It is best for the lenght is large but the elements are smaller
a=[2,13,4,2,9,9,5,8,7,13,3]
k=3
n=max(a)
b=[]
#OR b=[0]*n+1
#OR b=[0 for i in range(max(a)+1]
for i in range(n+1):
    b.append(0)
for i in a:
    b[i]=1

for i in range(len(b)-1,-1,-1):
    if b[i]==1:
        k-=1
    if k<=0:
        print(i)
        break

#with duplicates -->13,13,9,9,...--->3rd largest becomes 9
a=[2,13,4,2,9,9,5,8,7,13,3]
k=3
n=max(a)
b=[]
for i in range(n+1):
    b.append(0)
for i in a:
    b[i]+=1
c=0
for i in range(len(b)-1,-1,-1):
    if b[i]<=k:
        k-=b[i]
    else:
        print(i)
        break
    
#using merge sort---->list len small but elements large


    
    




