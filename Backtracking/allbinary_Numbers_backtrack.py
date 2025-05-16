#BackTrack
# print the binary numbers in the given number binary num len till the given number it should print
import math
res=[]
def binary(a,n,s=''):
    if len(s)==n:
        res.append(s)
        return
    binary(a,n,s+'0')
    binary(a,n,s+'1')
a=18
n=int(math.log(a,2))+1
binary(a,n)
for i in range(a+1):
    print(res[i])
    
#OR
def binary(a,n,s=''):
    if a==-1:
        return a
    if len(s)==n:
        print(s)
        a=a-1
        return a
    a=binary(a,n,s+'0')
    a=binary(a,n,s+'1')
    return a
a=18
n=int(math.log(a,2))+1
binary(a,n)
 
# def binary(n,s=''):
#     if n==0 and s==' ':
#         return '0'
#     if n==0:
#         return s
#     return binary(n//2,str(n%2)+s)
# def abc(n):
#     for i in range(n+1):
#         print(binary(i))
  
# n=int(input())
# abc(n)

