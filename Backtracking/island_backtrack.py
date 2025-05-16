#Finding the number of islands
''' 1 0 0 1
    1 1 0 1
    0 0 1 0 it will return 3 we should count if it has 1 s connected in left,right,top,bottom'''
#Back Tracking
def island(m,i,j,n):
    if i==n or j==n or i<0 or j<0 or m[i][j]==0 or m[i][j]==2:
        return 0
    if m[i][j]==1:
        m[i][j]==2  # to keep track of visited and come back not to fall in recursion loop
    
    island(m,i-1,j,n)
    island(m,i,j-1,n)
    island(m,i+1,j,n)
    island(m,i,j+1,n)

# n=int(input())
# m=[]
# for i in range(n):
#     m.append(list(map(int,input().split())))
m=[[1,0,0,1,1],[1,0,0,0,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,0,0,1]]
for i in m:
    print(i)
c=0
for i in range(5):
    for j in range(5):
        if m[i][j]==1:
            island(m,i,j,5)
    c+=1
print(c)
