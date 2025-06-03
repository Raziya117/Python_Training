#Max profit s-->time to work 
s=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
dp=a.copy()
for j in range(1,len(s)):
    for i in range(j):
        if s[i][1]<=s[j][0]:
            dp[j]=max(a[j]+dp[i],dp[j])
print(max(dp))