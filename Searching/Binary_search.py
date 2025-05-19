#BINARY SEARCH
#Find last occurence of key
a=[2,3,5,6,7,7,8,9,10,10,10,13,15]
key=10
l=0
h=len(a)-1
r=-1
while l<=h:
    mid=(l+h)//2
    if a[mid]==key:
        r=mid
        l=mid+1
        #h=mid-1-->first occurence
    elif key<a[mid]:
        h=mid-1
    elif key>a[mid]:
        l=mid+1
if r!=-1:
    print(r)
else:
    print(-1)