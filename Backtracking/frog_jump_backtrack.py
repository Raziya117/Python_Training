#Frog jump finding the number of steps to reach destination with hurdles given
def frog_jump(n,i,j,t):
    if i==n or j==n or (i,j) in t:
        return 0
    if i==n-1 and j==n-1:
        return 1
    return frog_jump(n,i+1,j,t)+frog_jump(n,i,j+1,t)

n=5
i=2
j=3
t=[(2,1),(4,1),(5,2),(3,5)]
print(frog_jump(n,i-1,j-1,t))

    
# n=int(input())
# l=int(input())
# m=int(input())
# t=tuple(map(int,input().split()))