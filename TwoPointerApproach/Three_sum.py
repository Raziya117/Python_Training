#Three sum
a=[-1,0,1,2,-1,-4]
a.sort()
b=[]
for i in range(len(a)):
    if i>0 and a[i]==a[i-1]:
            continue
    l=i+1
    r=len(a)-1
    
    while l<r:
        s=a[i]+a[l]+a[r]
        if s==0:
            b.append([a[i],a[l],a[r]])
            while l<r and a[l]==a[l+1]:
                l+=1
            while l<r and a[r]==[r-1]:
                r-=1
            l+=1
            r-=1
            
        elif s<0:
            l+=1
        else:
            r-=1
print(b)


            
            
