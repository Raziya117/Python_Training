#alphabets sorting
def sorting(a):
    for i in range(len(a)-1):
        flag=False
        for j in range(len(a)-i-1):
            if ord(a[j])>ord(a[j+1]):#if (a[j])>(a[j+1]):-->it alseo work same
                a[j],a[j+1]=a[j+1],a[j]
                flag=True
        if flag==False:
            break
    return a
a=['c','e','a','f']
print(sorting(a))




            