#Memorization
#o(2^n)
def fibo(n):
    if dp[n-1]!=-1:
        return dp[n-1]
    dp[n-1]=fib(n-1)+fib(n-2)
    return dp

#fibonacci nth value
#tabulation--->o(n)-space,time
'''dp=[1,1]
for i in range(2,7):
    dp.append(dp[i-1]+dp[i-2])
print(dp[7-1])'''

#or---Tabulation with space reduction
#o(n-2)-time,o(1)-space
f1=1
f2=1
ans=0
for i in range(2,7):
    ans=f1+f2
    f1=f2
    f2=ans
print(f2)