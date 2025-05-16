#Find second largest number
def even_odd(a):
    m1=0
    m2=0
    for i in a:
        if i>m1:
            m2=m1
            m1=i
        elif i>m2 and i!=m1:
            m2=i
    print(m2)
a=list(map(int,input().split()))
even_odd(a)