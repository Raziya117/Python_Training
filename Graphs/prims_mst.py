from collections import defaultdict
import heapq
def prims_mst(s):
    queue=[(0,s,-1)]
    visited=set()
    mcost=0
    r=[]
    while queue:
        wt,n,p=heapq.heappop(queue)
        if n in visited:
            continue
        visited.add(n)
        mcost+=wt
        if p!=-1:
            r.append((wt,p,n))
        for i,w in d[n]:
            if i not in visited:
                heapq.heappush(queue,(w,i,n))
                
    print(mcost)
    print(r)
                
                  
a=[(10,5,2),(10,7,4),(5,7,1),(5,8,3),(5,3,2),(7,8,1),(8,3,1)]
d=defaultdict(list)
d1=defaultdict(list)
for i,j,w in a:
    d[i].append((j,w))
    d[j].append((i,w))
prims_mst(10)