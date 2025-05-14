#Bitwise manipulation
#finding the single element from the array
li=[2,3,4,3,2,5,5]
d={}
for c in li:
    if c not in d:
        d[c]=1
    else:
        d[c]+=1
for k,v in dict.items(d):
    if v<2:
        print(k)
        
#or        
s=0
for i in li:
    s=s^i
print(s)
    