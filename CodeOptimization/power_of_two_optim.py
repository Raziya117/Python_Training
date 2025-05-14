# CHECKING IF IT IS THE POWER OF TWO OR NOT
#o(1)
n=int(input())
if n &(n-1)==0: 
    print('yes')
else:
    print('No')

#OR  --->o(logn)
i=0
while 1:  
    if 2**i==n:
        print('yes')
        break
    if n<2**i:
        print('no')
        break
    i+=1

#or --->O(logn)

while n%2==0:   
    n=n//2
if n==1:
    print('Yes')
else:
    print('No')
