#Finding the paths to reach the (n-1,n-1) from (0,0)
def rat_maze(m,i,j,n):
    if m[i][j]==0 or i==n or j==n:
        return 0
    if  i==n-1 or j==n-1 and m[i][j]==1:
        return 1
    return rat_maze(m,i,j+1,n)+rat_maze(m,i+1,j,n)

n=int(input())
m=[]
for i in range(n):
    m.append(list(map(int,input().split())))
print(rat_maze(m,0,0,n))