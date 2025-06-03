#min number of coins to get amount
coins=[2,3,4,5]
amt=12
dp=[[0]*(amt+1) for i in range(len(coins))]
dp[0][coins[0]]=1
for i in range(1,len(coins)):
    for j in range(1,amt+1):
        if j==coins[i]:
            dp[i][j]=1
        elif j<coins[i]:
            dp[i][j]=dp[i-1][j]
        else:
            if dp[i-1][j]!=0 and dp[i-1][j-coins[i]]!=0 :
                dp[i][j]=min(dp[i-1][j],dp[i-1][j-coins[i]]+1)
            elif dp[i-1][j]!=0:
                dp[i][j]=dp[i-1][j]
            elif dp[i-1][j-coins[i]]!=0:
                dp[i][j]=dp[i-1][j-coins[i]]+1

for i in dp:
    print(i)
print(dp[-1][-1])
