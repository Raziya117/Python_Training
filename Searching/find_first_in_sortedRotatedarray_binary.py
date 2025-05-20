a=[15,18,20,22,2,5,8,10,12,13]
#Binary search-O(logn)
l=0
r=len(a)-1
while l<r:
    m=(l+r)//2
    if a[m]<a[r]:
        r=m
    else:
        l=m+1
print(a[l])
#     elif a[l]<a[m]:
#         l=m+1
#     else:
#         print(a[r+1])
#         break
        
#LINEAR-->O(n)     
l=0
c=0
r=len(a)-1
while l<r:
    if a[l+1]>a[l]:
        l+=1
        c+=1
    else:
        break
if l==r:
    print(0) #IF array is not rotated
else:
    print(a[l+1],c+1)

#OR
r=0
for i in range(len(a)-1):
    if a[i+1]<a[i]:
        r=i+1
        break
print(r)

        