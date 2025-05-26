class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class linked:
    def __init__(self):
        self.head=None
        
    def add_back(self,x):
        new=node(x)
        if self.head==None:
            self.head=new
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new
            
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
        
    def sum(self):
        temp=self.head
        s=0
        while temp!=None:
            s=s+temp.data
            temp=temp.next
        print('sum of all nodes:',s)
        
    def even_sum(self):
        temp=self.head
        s=0
        while temp!=None:
            if temp.data%2==0:
                s+=temp.data
            temp=temp.next
        print('sum of all even nodes:',s)
        
    def even_pos_sum(self):
        temp=self.head
        s=0
        c=1
        while temp!=None:
            if c%2==0:
                s+=temp.data
            c+=1
            temp=temp.next
        print('sum of all even pos nodes:',s)
        
    def second_largest(self):
        temp=self.head
        m1=0
        m2=0
        while temp!=None:
            if temp.data>m1:
                m2=m1
                m1=temp.data
            elif temp.data>m2 and temp.data!=m1:
                m2=temp.data
            temp=temp.next
        print('second largest:',m2)
        
    def consecutive_sum_count(self,k):
        temp=self.head
        c=0
        while temp.next!=None:
            s=temp.data+temp.next.data
            if s<=k:
                c+=1
            temp=temp.next
        print('count:',c)
        
    def count_sum_target(self,k):
        temp=self.head
        c=0
        while temp.next!=None:
            curr=temp.next
            while curr!=None:
                if temp.data+curr.data<=k:
                    c+=1
                curr=curr.next
            temp=temp.next
        print('All posible sums:',c)
        
    def mid(self):
        #Floyds hare and tortoise
        f=self.head
        s=self.head
        #EVEN f!=None ODD-->f.next=None
        while f!=None and f.next!=None:
            f=f.next.next
            s=s.next
        print('Mid element:',s.data)
    
    def second_half(self):
        f=self.head
        s=self.head
        while f!=None and f.next!=None:
            f=f.next.next
            print(s.data,end='->') #First half
            s=s.next
        print('None')
        while s!=None:
            print(s.data,end='->')
            s=s.next
        print('None')
    
#         temp=self.head
#         c=1
#         while temp.next!=None:
#             c+=1
#             temp=temp.next
#         m=c//2
#         d=0
#         t=self.head
#         while t!=None:
#             if d>=m:
#                 print(t.data,end='->')
#             t=t.next
#             d+=1
#         print('None')
    
    def kthNode_last(self,k):
        f=self.head
        s=self.head
        for i in range(k):
            if f!=None:
                f=f.next
        while f!=None:
            f=f.next
            s=s.next
        if s!=None:
            print(s.data)
#         while f!=None:
#             if k<=3:
#                 f=f.next
#                 k-=1
#             f=f.next
#             s=s.next      
#         print(s.data)

    def delete_kth_node(self,k):
        f=self.head
        s=self.head
#         for i in range(k+1):
#             f=f.next
#         while f!=None:
#             s=s.next
#             f=f.next
#         s.next=s.next.next
        
        for i in range(k):
            f=f.next
        while f!=None:
            prev=s
            s=s.next
            f=f.next
        prev.next=s.next
    
    def swap(self):
        t=self.head
        while t!=None and t.next!=None:
            t.data,t.next.data=t.next.data,t.data
            t=t.next.next
            
    def bubbleSort(self):
        temp=self.head
        while temp.next!=None:
            f=0
            curr=self.head
            while curr.next!=None:
                if curr.data>curr.next.data:
                    curr.data,curr.next.data=curr.next.data,curr.data
                    f=1
                curr=curr.next
            if f==0:
                break
            temp=temp.next
            
    def kth_largest_element(self,k):
        temp=self.head
        k1=k
        while temp.next!=None and k!=0:
            f=0
            curr=self.head
            while curr.next!=None:
                if curr.data>curr.next.data:
                    curr.data,curr.next.data=curr.next.data,curr.data
                    f=1
                curr=curr.next
            if f==0:
                break
            temp=temp.next
            k-=1
        self.kthNode_last(k1)
        
    def check_loop_exists(self):
        f=self.head
        s=self.head
        while f!=None and f.next!=None:
            f=f.next.next
            s=s.next
            if f==s:
                print('Loop')
                return
            
        print('No loop')
        
    def even_odd_length(self):
        f=self.head
        s=self.head
        while f!=None and f.next!=None:
            f=f.next.next
            s=s.next
        if f==None:
            print('Even length')
        else:
            print('odd length')
        
        
        
obj=linked()
obj.add_back(9)
obj.add_back(3)
obj.add_back(10)
obj.add_back(11)
obj.add_back(5)
obj.add_back(12)
obj.add_back(50)
obj.add_back(90)
'''obj.display()
obj.sum()
obj.even_sum()
obj.even_pos_sum()
obj.second_largest()
obj.consecutive_sum_count(30)
obj.count_sum_target(30)
obj.mid()
obj.second_half()
obj.kthNode_last(5)
obj.delete_kth_node(3)
obj.display()
obj.swap()'''
obj.display()
obj.bubbleSort()
obj.display()
obj.kth_largest_element(4)
obj.check_loop_exists()
obj.even_odd_length()
l2=linked()
l2.head=node(100)
l2.head.next=node(10)
l2.head.next.next=node(20)
l2.head.next.next.next=node(30)
l2.head.next.next.next=l2.head.next
l2.check_loop_exists()