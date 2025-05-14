# count of each charcter printing in the same line
#s='aaabbaaaacccddeff'------>o/p:a3b2a4...
s='abbacbababc'
t=''
c=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        t+=s[i]+str(c)
        c=1
t+=s[-1]+str(c)
print(t)