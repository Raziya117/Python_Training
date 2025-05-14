# if a number is given then doing xor in its range ex:5---->1^2^3^4^5
# O(n)
s=0   
for i in range(1,n+1):
    s=s^i
print(s)

#OR ---> O(1)
if n%4==1: 
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)
else:
    print(n)

# perfoming xor between a given range ex:5  10 ---->5^6^7^8^9^10
#o(n)
n=int(input())
m=int(input())
s=0
for i in range(n,m+1):
    s=s^i
print(s)

#OR  ----> o(1)
def n_xor(n):
    if n%4==1:
        return 1
    elif n%4==2:
        return n+1
    elif n%4==3:
        return 0
    else:
        return n
n=int(input())
m=int(input())
print(n_xor(n-1)^n_xor(m))
