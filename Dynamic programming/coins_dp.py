#given 2,3 4,5 are the coins now can we make 13 by using these coins is it possible or not
coins=[2,3,4,5]
amt=11
# if amt>sum(coins):
#     return 'Not'
dp=[[0]*(amt+1) for i in range(len(coins))]
for i in range(len(coins)):
    dp[i][0]=1
dp[0][coins[0]]=1
for i in range(1,len(coins)):
    for j in range(1,amt+1):
        if j<coins[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j] or dp[i-1][j-coins[i]]
            
#         elif dp[i-1][j]==1:
#             dp[i][j]=dp[i-1][j] 
#         else:
#             if dp[i-1][j-coins[i]]==1:
#                 dp[i][j]=dp[i-1][j-coins[i]]
for i in dp:
    print(i)
if dp[-1][-1]==1:
    print('pos')
else:
    print('Not pos')