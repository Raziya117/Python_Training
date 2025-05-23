a=[5,5,10]
five=0
ten=0
for i in a:
    if i==5:
        five+=1
    elif i==10:
        if five>0:
            ten+=1
            five-=1
        else:
            print('Not possible')
            break
    elif i==20:
        if five>0 and ten>0:
            five-=1
            ten-=1
        elif five>=3:
            five-=3
        else:
            print('Not possible')
            break
else:
    print('possible')
    
        
    