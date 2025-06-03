from collections import defaultdict
import heapq
def krushkals_mst(a):
    a.sort(key=lambda x:x[2])
    print(a)
    p={}
    nodes=set()
    mc=0
    res=[]
    for i,j,w in a:
        nodes.add(i)
        nodes.add(j)
    for n in nodes:
        p[n]=n
    def find(x):
        if p[x]!=x:
            p[x]=find(p[x])
        return p[x]
    def union(u,v):
        x,y=find(u),find(v)
        if x==y:
            return False
        p[y]=x
        return True
    for i,j,w in a:
        if union(i,j):
            res.append((i,j,w))
            mc+=w
    print(mc,res)
        
        
a=[(10,5,2),(10,7,4),(5,7,1),(5,8,3),(5,3,2),(7,8,1),(8,3,1)]
d=defaultdict(list)
for i,j,w in a:
    d[i].append([j,w])
    d[j].append([i,w])
krushkals_mst(a)
    