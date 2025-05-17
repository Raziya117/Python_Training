#sort the words in sentence by the length of word
#s.sort(key=len)-->direct
def length(w):
    c=0
    for _ in range(len(w)):
        c+=1
    return c

def sorting(a,b):
    for i in range(len(b)-1):
        f=0
        for j in range(len(b)-i-1):
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
                a[j],a[j+1]=a[j+1],a[j]
                f=1
        if f==0:
            break
    return a
          
            
s='An apple a day keeps the doctor away'
w=s.split()
b=[]
for i in w:
    b.append(length(i))#b.append(len(i))
q=sorting(w,b)
#r=' '.join(q)
print(*q)