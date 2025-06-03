s='15,-3,+,6,2,-,*'
a=s.split(',')
stack=[]
for i in a:
    if i[-1].isdigit():
        stack.append(int(i))    
    else:
        f=stack.pop()
        sec=stack.pop()
        if i=='+':
            res=sec+f
        elif i=='-':
            res=sec-f
        elif i=='*':
            res=sec*f
        elif i=='/':
            res=sec/f
        else:
            res=sec**f
        stack.append(res)
print(stack[-1])

      
        
    