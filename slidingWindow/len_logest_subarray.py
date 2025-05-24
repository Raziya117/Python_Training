#length of longest sub array where sum<=k:(sliding window)
#O(n^2):
a=[2,1,4,6,2,3,1,1,4,2,6,7,3]
k=7
leng=0
for i in range(len(a)):
    sum1=0
    for j in range(i,len(a)):
        sum1+=a[j]
        if sum1<=k:
            leng=max(leng,j-i+1)
        else:
            break
print(leng)



#OR------O(n)
a=[2,1,4,6,2,3,1,1,4,2,6,7,3]
k=7
i=0
sum1=0
leng=0
for j in range(len(a)):
    sum1+=a[j]
    while sum1>k:
        sum1-=a[i]
        i+=1
    leng=max(leng,j-i+1)
print(leng)


#OR-----O(n)
a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=7
sum=0
length=0
l=0
r=0
while r<len(a):
    sum+=a[r]
    while sum>k and l<=r:
        sum-=a[l]
        l+=1
    if sum<=k:
        length=max(length,r-l+1)
    r+=1
print(length)
