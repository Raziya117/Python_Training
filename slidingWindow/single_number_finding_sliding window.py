#SLIDING WINDOW
# finding the single frequenecy number Ex:[2,2,3,3,4,5,5]---->o/p:4
a=list(map(int,input().split()))
for i in range(0,len(a)-1,2):
    if a[i]!=a[i+1]:
        print(a[i])
        break
else:
    print(a[-1])




        
    
    
        
        
    

