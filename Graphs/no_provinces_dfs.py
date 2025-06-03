#No of disconnected graphs slef loops should be ignored
def provinces(i,l,a,n):
    l[i]=True
    for j in range(n):
        if a[i][j]==1 and i!=j and l[j]!=True:
            provinces(j,l,a,n)
    
        
a=[[1,1,0],[1,1,0],[0,0,1]]
n=len(a)
l=[False]*n
c=0
for i in range(n):
    if l[i]==False:
        c+=1
        provinces(i,l,a,n)
print(l)
        
print(c)

        
