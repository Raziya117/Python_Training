# checking whether a num is prime or not if it is prime then we need to check if it is < 200 or not
n=int(input())
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(f'{n} is not a prime number')
        else:
            if n>200:
                print(f'{n} is greater than 200')
            else:
                print(f'{n} is less than 200')            
prime(n)



        
        
        
        