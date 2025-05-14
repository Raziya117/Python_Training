# find the missing number from the given list Ex:[0,1,2,4]-->missing num is 3
def find_missing(li):
    n=len(li)
    s=0
    t=0
    for c in li:
        s=s^c
    
    for i in range(n+1):
        t=t^i
    return t^s
li=[0,1,3,4]
b=find_missing(li)
print(b)
