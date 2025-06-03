# possibpe or not if infinite number of coins are there
# coins=[2,3,4,5]
# amt=12
# dp=[[0]*(amt+1) for i in range(len(coins))]
# for i in range(len(coins)):
#     dp[i][0]=1
# for i in range(len(coins)):
#     for j in range(1,amt+1):
#         if j<coins[i]:
#             dp[i][j]=dp[i-1][j]
#         elif dp[i-1][j]==1:
#             dp[i][j]=dp[i-1][j]
#         elif dp[i][j-coins[i]]==1:
#             dp[i][j]=dp[i][j-coins[i]] 
# for i in dp:
#     print(i)

# min coins--->infinite coins
coins=[2,3,4,5]
amt=13
dp=[0]*(amt+1)
for i in coins:
    for j in range(i,amt+1):
        if i==j:
            dp[j]=1
        if dp[j]!=0 and dp[j-i]!=0:
            dp[j]=min(dp[j],dp[j-i]+1)
        elif dp[j-i]!=0:
            dp[j]=dp[j-i]+1     
print(dp)
            

            
            
        
    
    


        
        