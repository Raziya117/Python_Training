#Buying for small price and selling for more profit
# O(N)
a=[13,14,2,5,8,1,4]
mp=0
buy=a[0]
for i in range(1,len(a)):
    if a[i]>buy:
        if a[i]-buy>mp:
            mp=a[i]-buy
    else:
        buy=a[i]
print(mp)

#OR -->TWO POINTER-->O(N*N)
a=[13,14,2,5,8,1,4]
mp=0
for i in range(len(a)-1):#Buy price
    for j in range(i+1,len(a)):#sell price
        if a[j]-a[i]>mp:
            mp=a[j]-a[i]
print(mp)

#OR---->extra space
a=[13,14,2,5,8,1,4]
mp=0
b=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>mp:
            b.append(a[j]-a[i])
print(max(b))

#OR
a=[13,14,2,5,8,1,4]
mp=0
b=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
            b.append(a[j]-a[i])
print(max(b))
               
