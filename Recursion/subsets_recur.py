#Printing the subsets
def subset(a,x=[],i=0):
    if i==len(a):
        print(x)
        return
    subset(a,x+[a[i]],i+1)
    subset(a,x,i+1)

a=[2,3,4]
subset(a)