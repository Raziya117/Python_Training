#sort according to the second element in the matrix
def sort(a):
    for i in range(len(a)-1):
        flag=False
        for j in range(len(a)-i-1):
            if a[j][1]>a[j+1][1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=True
        if flag==False:
            break
    return a
            
    
a=[[2,3],[5,1],[1,4],[2,7],[1,7]]
print(len(a))
print(sort(a))