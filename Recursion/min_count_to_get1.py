#4.printing is it possible to reach 1 by subtracting a number
def pos(x,n,m):
    if x==1:
        return True
    if x<1:
        return False
    else:
        return pos(x-n,n,m) or pos(x-m,n,m,)
x=20
n=3
m=5
print(pos(x,n,m))

#printing is it possible to reach 1 by subtracting a two umbers ex:3,5 from 20--->1 min subtraction count to reach one

def pos(x,n,m,c=0):
    if x==1:
        return 0
    if x<1:
        return False
    else:
        return 1+min(pos(x-n,n,m,c+1),pos(x-m,n,m,c+1))
x=20
n=3
m=5
print(pos(x,n,m))