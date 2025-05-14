#TIME COMPLEXITY-OPTIMIZATION
# REMOVING DUPLICATE NUMBERS FROM A ARRAY
# O(N*N)
def remove_duplicate(nums):
    li=[]
    for i in nums:
        if i not in li:
            li.append(i)
    print(li)
nums=list(map(int,input().split()))               
remove_duplicate(nums)
    
#O(N)
def remove_duplicate(nums):
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
nums=list(map(int,input().split()))               
remove_duplicate(nums)
