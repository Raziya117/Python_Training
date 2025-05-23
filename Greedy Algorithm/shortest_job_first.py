#shortest job first
a=[4,3,7,1,6,2]
a.sort()
wait=0
curs=0
for i in range(len(a)-1):
        curs+=a[i]
        wait+=curs
    
avg=wait//len(a)
print(avg)

    
    
    
    