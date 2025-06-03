#FInd the min subarray length which must be equal to target
a=[2,3,1,2,4,3]
t=7
l=0
m=9999999
s=0
st=0
for r in range(len(a)):
    s+=a[r]
    while s>=t:
        m=min(m,r-l+1)
        st=l
        s-=a[l]
        l+=1
print(m,a[st:st+m])
    
        
    