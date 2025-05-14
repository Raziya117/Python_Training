#3.prime numbers
def prime(i,x):
    if i==((x//2)+1):
        return True
    if x%i==0:
        return False
    return prime(i+1,x)
       
def count_prime(a,c,i):
    if i==len(a):
        return c
    if prime(2,a[i]):
        return count_prime(a,i+1,c+1)
    return count_prime(a,i+1,c)
        
    

a=[13,17,21,23,22,7,29]
print(count_prime(a,0,0))