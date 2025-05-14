#2.reverse

def reverse(r,n):
    if n==0:
        return r  
    return reverse(r*10+n%10,n//10)
n=54427
print(reverse(0,n))