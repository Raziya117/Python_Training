#Finding hte frequenecy of given number
#1.parametraized recursion ---->return c
def count(a,k,i,c=0):
    if i==len(a):
        return c
    elif a[i]==k:
        return count(a,k,i+1,c+1)
    else:
        return count(a,k,i+1,c)
        
a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=6
b=count(a,k,0)
print(b)

#OR 2
def count(a,k,i,c=0):
    if i==len(a):
        return c
    elif a[i]==k:
        c+=1
    return count(a,k,i+1,c)
        
a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=6
print(count(a,k,0))

#OR --->functional recursion--->return 0
a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=6
def freq(a,k,i=0):
    if i==len(a):
        return 0
    if a[i]==k:
        return 1+freq(a,k,i+1)
    else:
        return freq(a,k,i+1)
print(freq(a,k))
