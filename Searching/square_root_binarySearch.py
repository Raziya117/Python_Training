#Find the square root of a number
#x=n**0.5
# O(logn)
n=38
#n=0
#h=n
l=1
h=n//2
res=-1
while l<=h:
    mid=(l+h)//2
    if mid*mid==n:
        res=mid
        break
    elif mid*mid<n:
        res=mid #if we didnt keep we will print outside print(r)-->if it is floor -->if it is ceil -->print(l)
        l=mid+1
    elif mid*mid>n:
        h=mid-1
print(res)

#OR--linear-->O(n)
for i in range(1,n//2):
    if i*i==n:
        print(i)
        break
    elif i*i>n:
        print(i-1)
        break
        
    
    