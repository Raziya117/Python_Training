#Jump game
#checking the possibilty to reach last posistion
a=[2,3,1,1,4]
m=0
for i in range(len(a)-1):
    if i>m:
        print('Not possible')
        break
    if i+a[i]>m:
        m=i+a[i]
else:
    print('Possible')


#OR
a=[2,3,1,1,4]
l=0
r=0
c=0
f=0
while r<len(a)-1:
    m=0
    for i in range(l,r+1):
        if i+a[i]>m:
            m=i+a[i]
        if m>=len(a):
            f=1
            break
        
    l=r+1
    r=m
    c+=1
    if f==1:
        break
    
print(c)

      
# print the minimum jumps
a=[2,3,1,1,4]
m=0
c=0
end=0
for i in range(len(a)-1):
    if i+a[i]>m:
        m=i+a[i]
    if i==end:
        c+=1
        end=m
print(c)