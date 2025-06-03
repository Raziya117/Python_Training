def jump(a,i):
    if i==0:
        return 0
    if i==1:
        return abs(a[1]-a[0])
    l= jump(a,i-1)+abs(a[i]-a[i-1])
    r=jump(a,i-2)+abs(a[i]-a[i-2])
    return min(l,r)

a=[10,20,30,10]
print(jump(a,len(a)-1))

#dp
#Memorization
def jump(n):
    if n<=1:
        return dp[n]
    dp[n]=min(jump(n-1)+abs(a[n]-a[n-1]), jump(n-2)+abs(a[n]-a[n-2]))
    return dp[n]

a=[10,20,30,10,30,20,10]
dp=[0,abs(a[1]-a[0]),0,0,0,0,0]
n=6
jump(n)
print(dp[n])

#Tabulation
a=[10,20,30,10,30,20,10]
dp=[0]*len(a)
dp[1]=abs(a[1]-a[0])
for i in range(2,len(a)):
    dp[i]=min(dp[i-1]+abs(a[i-1]-a[i]),dp[i-2]+abs(a[i-2]-a[i]))
print(dp[len(a)-1])

# OR
#Tabulation with memory efficient
x=0
y=abs(a[1]-a[0])
res=0
for i in range(2,len(a)):
    res=min(y+abs(a[i-1]-a[i]),x+abs(a[i-2]-a[i]))
    x=y
    y=res
print(y)

#k jumps
a=[10,20,30,10,30,20,10]
k=2
dp=[9999]*len(a)
dp[1]=abs(a[0]-a[1])
for i in range(2,len(a)):
    for j in range(1,k+1):
        ans=dp[i-j]+abs(a[i-j]-a[i])
        dp[i]=min(ans,dp[i])
    
print(dp[len(a)-1])
    




    
    
        