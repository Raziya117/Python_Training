#Bubble sort
#Most Efficient
def bubble(a,n):
    for i in range(n-1):
        flag=False   # #it will stops once it is sorted without repeating n-1 times 
        for j in range(n-1-i): # keeping -i reduces the number of checking beacuse every check the last element is sorted
            if a[j]>a[j+1]:
                flag=True
                a[j],a[j+1]=a[j+1],a[j]
        if flag==False:
            break
    return a
a=[2,3,4,9,1]
n=len(a)
print(bubble(a,n))

# Or 
# def bubble(a,n):
#     for i in range(n-1):
#         for j in range(n-1):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     return a
# a=[2,3,4,9,1]
# n=len(a)
# print(bubble(a,n))

#sort middle elements without changing k elements front and back
def bubble(a,n,k):
    for i in range(k,n-k):
        flag=False
        for j in range(k,n-k-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=True
        if flag==False:
            break
        print(a)
    return a
    
a=[5,2,3,8,1,6,7]
n=len(a)
k=2
print(bubble(a,n,k))
# bubble(a,n,k)

#Kth largest element
def bubble(a,n):
    c=0
    for i in range(k): #for i in range(n-1):#if we keep n total checkings=10 for k--->9
        flag=False    
        for j in range(n-1-i):
            c+=1
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=True
#         k-=1
        if flag==False: #if flag==False or k==0:
            break
    print(c)
    return a[-k]
a=[2,5,8,6,3,1,9,4,7]
n=len(a)
k=3
print(bubble(a,n))


    