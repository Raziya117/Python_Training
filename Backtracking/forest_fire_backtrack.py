#Forest fire 
def land(a,i,j,n):
    if i<0 or j<0 or i==n or j==n or a[i][j]==0 or a[i][j]==2:
        return 0
    if m[i][j]==1:
        m[i][j]==2
    
    land(m,i-1,j,n)
    land(m,i,j-1,n)
    land(m,i+1,j,n)
    land(m,i,j+1,n)
        
m=3
o=6
a=[[1,0,0,1,1,1],[1,1,1,0,0,0],[0,0,1,1,1,1],[1,1,1,0,0,0],[0,0,0,0,0,1],[1,0,0,1,0,0]]
land(a,2,5,5)
c=0
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            c+=1
print(c)

#OR
def fire_catch(m,i,j,n=None):
    if n==None:
        n=len(m)
    if i>=n or j>=n or i<0 or j<0 or m[i][j]==0 or m[i][j]==2 :
        return 0
    if m[i][j]==1:
        m[i][j]=2
        
    fire_catch(m,i-1,j,n)
    fire_catch(m,i+1,j,n)
    fire_catch(m,i,j+1,n)
    fire_catch(m,i,j-1,n)
m=[]
n=int(input())
for _ in range(n):
    m.append(list(map(int,input().split())))
c=0
fire_catch(m,2,5,n)
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            c+=1

        
print(c)

'''6
1 0 0 1 1 1
1 1 1 0 0 0
0 0 1 1 1 1
1 1 1 0 0 0
0 0 0 0 0 1
1 0 0 1 0 0
'''


        
