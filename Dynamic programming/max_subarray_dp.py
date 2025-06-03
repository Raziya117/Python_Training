a=[-2,1,-3,4,-1,2,1,-5,4]
dp=[0]*len(a)
m=a[0]
dp[0]=a[0]
for i in range(1,len(a)):
    dp[i]=max(a[i],dp[i-1]+a[i])
    m=max(m,dp[i])
print(m)
print(dp)