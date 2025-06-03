a=[2,3,4,1,5,6,7]
a.sort()
t=19
found=False
for i in range(len(a)-3):
    for j in range(i+1,len(a)-2):
        l=i+1
        r=len(a)-1
        while l<r:
            for k in range(l+1,r):
                while l<r:
                    s=a[i]+a[k]+a[l]+a[r]
                    if s==t:
                        print('true',a[i],a[k],a[l],a[r])
                        found=True
                        break
                    elif s<t:
                        l+=1
                    else:
                        r-=1
        if found:
            break
    if found:
            break
if not found:
        print('Not found')
                    
            
            