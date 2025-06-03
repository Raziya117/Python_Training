class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
        
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data,end=' ')
        self.inorder(root.right)
        
    def preorder(self,root):
        if root==None:
            return
        print(root.data,end=' ')
        self.inorder(root.left)
        self.inorder(root.right)
        
    def postorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.data,end=' ')
    
    def sum_all(self,root):
        if root==None:
            return 0
        return root.data + self.sum_all(root.left) + self.sum_all(root.right)
    
    def even_sum(self,root):
        if root==None:
            return 0
        elif root.data%2==0:
            return root.data + self.even_sum(root.left) + self.even_sum(root.right)
        else:
            return  self.even_sum(root.left)+self.even_sum(root.right)
    
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    
    def search(self,root,key):
        if root==None:
            return'not'
        elif key==root.data:
            return 'element found'
        elif key<root.data:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
    #dfs 
    def count_leafnodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.count_leafnodes(root.left)+self.count_leafnodes(root.right)
    
    def print_paths(self,root,l):
        if root==None:
            return
        l.append(root.data)
        if root.left==None and root.right==None:
            print(l)
            l.pop()
            return
        self.print_paths(root.left,l)
        self.print_paths(root.right,l)
        l.pop()
        return l
    
    #Bfs
    def level_order(self,root,l):
        if root==None:
            return
        l.append(root)
        while l:
            curr=l.pop(0)
            if curr.left!=None:
                l.append(curr.left)
            if curr.right!=None:
                l.append(curr.right)
            print(curr.data,end=' ')
            
            
    def count_leaf_level(self,root,l):
        if root==None:
            return
        l.append(root)
        c=0
        while l:
            curr=l.pop(0)
            if curr.left!=None:
                l.append(curr.left)
            if curr.right!=None:
                l.append(curr.right)
            if curr.left==None and curr.right==None:
                c+=1
        print(c)
        
    def left_view(self,root,c=0,d={}):
        if root==None:
            return 
        if c not in d:
            d[c]=root.data
            print(d[c],end=' ')
        self.left_view(root.left,c+1,d)
        self.left_view(root.right,c+1,d)
    
    def right_view(self,root,c=0):
        if root==None:
            return
        d[c]=root.data
        self.right_view(root.left,c+1)
        self.right_view(root.right,c+1) 
        
    def top_view(self,root):
        c=0
        l=[(root,c)]
        d={}
        while l:
            curr,c=l.pop(0)
            if c not in d:
                d[c]=curr.data
            if curr.left!=None:
                l.append((curr.left,c-1))
                
            if curr.right!=None:
                l.append((curr.right,c+1))
        for i in sorted(d):
            print(d[i],end=' ')
    
    def bottom_view(self,root):
        c=0
        l=[(root,c)]
        d={}
        while l:
            curr,c=l.pop(0)
            d[c]=curr.data
            if curr.left!=None:
                l.append((curr.left,c-1))
                
            if curr.right!=None:
                l.append((curr.right,c+1))
        for i in sorted(d):
            print(d[i],end=' ')
    #for bst        
    def lowcommon_ancestor(self,root,p,q):
        if root==None:
            return None
        if p<root.data and q<root.data:
            self.lowcommon_ancestor(root.left,p,q)
        elif p>root.data and q>root.data:
            self.lowcommon_ancestor(root.right,p,q)
        else:
            return root.data
        
    #For binary tree
    def low_common(self,root,p,q):
        if root==None:
            return
        if p==root.data or q==root.data:
            return root
        l=self.low_common(root.left,p,q)
        r=self.low_common(root.right,p,q)
        if l!=None and r!=None:
            return root.data
        if l!=None:
            return l
        else:
            return r
        
    def balanced_or_not(self,root):
        if root==None:
            return True
        l=self.height(root.left)
        r=self.height(root.right)
        if abs(l-r)>1:
            return False
        return self.balanced_or_not(root.left) and self.balanced_or_not(root.left)      
   
    def insert(self,root,x):
        if root==None:
            return node(x)
        if x<root.data:
            root.left=self.insert(root.left,x)
        else:
            root.right=self.insert(root.right,x)
        return root    
            
root=None           
root=node(10)
root=root.insert(root,5)
root=root.insert(root,20)
root=root.insert(root,2)
root=root.insert(root,8)
# root=node(10)
# root.left=node(5)
# root.right=node(20)
# root.right.left=node(19)
# root.left.left=node(2)
# root.left.right=node(8)
root.inorder(root)
# print()
# root.preorder(root)
# print()
# root.postorder(root)
# print(f'\nsum of all: {root.sum_all(root)}')
# print(f'sum of even: {root.even_sum(root)}')
# print('height:',root.height(root))
# print(root.search(root,12))
'''print(root.count_leafnodes(root))
root.print_paths(root,[])
root.level_order(root,[])
print()
root.count_leaf_level(root,[])
print('\nleft view:')
root.left_view(root)
print('\nright view:')
d={}

root.right_view(root)

for i in d:
    print(d[i],end=' ')
print('\nTop view')
root.top_view(root)
print('\nBottom view')
root.bottom_view(root)
print('\n',root.lowcommon_ancestor(root,2,20))
print(root.low_common(root,2,8))
print(root.balanced_or_not(root))'''
