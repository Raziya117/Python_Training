#find the maximum no of meeting can be conducted if a and b are the starting and ending times of meetings
def meet(x):
    return x[1]
a=[0,3,8,1,5,7,9]
b=[5,6,10,2,6,9,11]
c=list(zip(a,b))
c.sort(key=meet)
count=0
starttime=0
for i in c:
    if i[0]>=starttime:
        count+=1
        starttime=i[1]+1
print(count)
