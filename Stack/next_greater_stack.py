#Next greater element.a is always a subset of b and for every element in a we need  to find the next immediate greater element in b
a=[4,1,2]
b=[2,1,3,4]
stack=[]
d={}
for i in b:
    while stack and i>stack[-1]:
        p=stack.pop()
        d[p]=i
    stack.append(i)
for i in stack:
    d[i]=-1
r=[d[i] for i in a]
print(r)