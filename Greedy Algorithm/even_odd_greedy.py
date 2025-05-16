#Finding ht largest evn number and smallest odd
#Greedy algorithm
def even_odd(a):
    me=0
    mo=99999
    for i in a:
        if i>me and i%2==0:
            me=i
        else:
            if i<mo and i%2!=0:
                mo=i
    print(me,mo)
a=list(map(int,input().split()))
even_odd(a)