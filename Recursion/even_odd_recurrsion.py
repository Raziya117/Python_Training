#RECURRSION
#1.even or odd
def even_sum(x,i):
    if i==len(x):
        return 0
    elif x[i]%2==0:
        return x[i]+even_sum(x,i+1)
    else:
        return even_sum(x,i+1)
  
a=[2,5,6,7,2,1,4,3,6]
print(even_sum(a,0))










