#sort 2d matrix according to the prime numbers in the each row
#I/p:[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]--->O/p:[[14,8,3],[8,10,5],[7,9,20],[4,13,12]]
def prime(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            return i
    
def bubble(a,b):
    for i in range(len(b)-1):
        flag=False   
        for j in range(len(b)-1-i):
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
                a[j],a[j+1]=a[j+1],a[j]
                flag=True
        if flag==False:
            break
    print(a)
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
b=[]
for i in a:
    b.append(prime(i))
bubble(a,b)
