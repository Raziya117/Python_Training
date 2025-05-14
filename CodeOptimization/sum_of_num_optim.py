# TIME COMPLEXITY-OPTIMIZATION
# SUM OF NUMBERS-->O(1)
n=int(input())
s=n*(n+1)//2#o(1)
print(s)

# O(N)
sum=0
fact=1
for i in range(1,n+1):
    sum+=i
    fact*=i
print(sum)
print(fact)
