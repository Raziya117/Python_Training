#single source shortest path-sssp
from collections import defaultdict
def dijkstras_sp(s,u):
    q=[s]
    v=set()
    d1=defaultdict(lambda:float('inf'))
    d1[s]=0
    c=0
    sp=defaultdict(int)
    sp[s]=s
    while q:
        curr=q.pop(0)
        v.add(curr)
        for i,w in d[curr]:
            c=d1[curr]+w
            if c<d1[i]:
                d1[i]=c
                sp[i]=curr
            if i not in v and i not in q:
                q.append(i)
            
    print(d1)
    l=[u]
    while sp[u]!=u:
        l.append(sp[u])
        u=sp[u]
    print(l[::-1])
    
            
    
a=[(10,5,2),(10,7,4),(5,7,1),(5,8,3),(5,3,2),(7,8,1),(8,3,1)]
d=defaultdict(list)
d1=defaultdict(list)
for i,j,w in a:
    d[i].append([j,w])
    d[j].append([i,w])
dijkstras_sp(10,3)
# s=10
# for i in d:
#     if i==s:
#         d1[i]=0
#     else:
#         d1[i]=float('inf')
# print(d)

