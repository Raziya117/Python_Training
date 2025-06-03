s='(a+b)-c*d'
a=list(s)
stack=[]
res=''
p={'+':1,'-':1,'*':2,'/':2,'^':3}
for i in a:
    if i.isalpha():
        res+=i
    elif i=='(':
        stack.append(i)
    elif i==')':
        while stack and stack[-1]!='(':
            res+=stack.pop()
        stack.pop()
    else: 
        while stack and stack[-1]!='(' and p.get(i,0)<=p.get(stack[-1],0) :
                res+=stack.pop()
        stack.append(i)
while stack:
    res+=stack.pop()
print(res)
         
            
        
