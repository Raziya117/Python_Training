#car petrol possibility
#a=[2,2,1,0,1,3,0]-->not
a=[2,3,1,0,1,3,0]#-->yes
p=0
for i in range(len(a)):
    if p<0:
        print('not possible')
        break
        
    p=max(p,a[i])
    p-=1
else:
    print('possible')
    
        