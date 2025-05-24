##discounts=[2,1,6,4,2,3,1,1,4,2,6,7,3] take continuous elements to get max discounts(sliding window)
a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=5
start=0
sum1=sum(a[:k])
max1=sum1
for i in range(k,len(a)):
    sum1=sum1-a[i-k]+a[i]
    if sum1>max1:
        max1=sum1
        start=i-k+1
print(max1)
print(a[start:start+k])
    