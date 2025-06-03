from collections import defaultdict
#DFS
def print_all_paths(u,v,path=[]):
    path.append(u)
    if u==v:
        print(path)
#         path.pop()
#         return
    for i in d[u]:
        if i not in path:
            print_all_paths(i,v,path)
    path.pop()  
    return

def path_exists(u,v,path=set()):
    if u==v:
        return True
    path.add(u)
    for i in d[u]:
        if i not in path:
            if path_exists(i,v,path):
                return True
    return False

def count_all_paths(u,v,path=set(),c=0):
    path.add(u)
    if u==v:
        c+=1
    for i in d[u]:
        if i not in path:
            c=count_all_paths(i,v,path,c)
    path.remove(u)  
    return c

def len_of_allpaths(u,v,path=[],c=0):
    path.append(u)
    if u==v:
        print(path,c+1)
    for i in d[u]:
        if i not in path:
            c=c+1
            len_of_allpaths(i,v,path,c)
            c=c-1
    path.pop()  
    return 
#BFS
def BFS(u):
    v={u}
    q=[u]
    while q:
        c=q.pop(0)
        print(c,end=' ')
        for i in d[c]:
            if i not in v and i not in q:
                v.add(i)
                q.append(i)
                
def BFS_path_exists(x,y):
    v={x}
    q=[x]
    while q:
        curr=q.pop(0)
        if curr==y:
            return True
        for i in d[curr]:
            if i not in v:
                v.add(i)
                q.append(i)
    return False

def min_path(u,v,path=[]):
    q=[u]
    vi=set()
    while q:
        c=q.pop(0)
        for i in d[c]:
            if i not in vi:
                vi.add(i)
                q.append(i)
                
          
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i) #directed graph no need this line

print_all_paths(5,3)
print(count_all_paths(5,3))
len_of_allpaths(5,3)
print(path_exists(5,3))

BFS(5)

print(BFS_path_exists(5,3))















#OR
# d={}
# for i,j in graphs:
#     if i not in d:
#         d[i]=[j]
#     else:
#         d[i].append(j)
#     if j not in d:
#         d[j]=[i]
#     else:
#         d[j].append(i)
# print(d)