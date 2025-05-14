#finding the maximum subarray average

def maxAvg(li,k):
    csum=0
    for i in range(k):
        csum+=li[i]
    msum=csum
    for i in range(k,len(li)):
        csum+=li[i]-li[i-k]
        if csum>msum:
            msum=csum
    return msum//k
li=[1,2,3,4,5]
k=3
b=maxAvg(li,k)
print(b)
    