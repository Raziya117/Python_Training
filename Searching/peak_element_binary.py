#Find the peak element--->prev and next elkement should be less than curr element
#Binary search
a=[8,2,3,4,6,3,2,1,5,8,10,1,4,2]
l=0
r=len(a)-1
while l<=r:
    m=(l+r)//2
    if m==0 or a[m]>a[m-1] and m==len(a)-1 or a[m]>a[m+1]:
        print(a[m])
        break
    if a[m+1]>a[m]:
        l=m+1
    else:
        r=m-1
#OR
a=[8,2,3,4,6,3,2,1,5,8,10,1,4,2]
for i in range(1,len(a)-1):
    if a[i-1]<a[i] and a[i+1]<a[i]:
        print(a[i])

    
        
    
