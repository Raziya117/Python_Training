l='(({}))'
a=list(l)
s=[]
for i in a:
    if i in {'(','[','{'}:
        s.append(i)
    elif s:
        if (i==')'and s[-1]=='(') or (i=='}' and s[-1]=='{') or (i==']' and s[-1]=='['):
            s.pop()
        else:
            print('Invalid')
            break
    else:
        print('Invalid')
        break
else:
    if s:
        print('Not valid')
    else:
        print('valid')

#Using dictionary
l='(({}))'
a=list(l)
stack=[]
d={')':'(',']':'[','}':'{'}
for i in a:
    if i in {'(','[','{'}:
        stack.append(i)
    else:
        if stack and d[i]==stack[-1]:
                stack.pop()
        else:
            print('Invalid')
            break
else:
    if s:
        print('Invalid')
    else:
        print('Valid')
    
            