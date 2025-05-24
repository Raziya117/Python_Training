#find the length of longest palindromic substring;
#O(n^3)
s="ababba"
res=[]
max_len=0

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        res.append(s[i:j])
        
# print(res)
for i in res:
    if i==i[::-1]:
        max_len=max(max_len,len(i))
print(max_len)


#OR(best)
#shrinking sliding window
s="ababba"
m=0
start=0  #(to find the palindrome)
c=0
for i in range(len(s)):
    l=i
    r=i
    while(l>=0 and r<len(s) and s[l]==s[r]):
        if(m<r-l+1):
            m=r-l+1
            start=l
        c+=1
        l-=1
        r+=1
    l=i
    r=i+1
    while(l>=0 and r<len(s) and s[l]==s[r]):
        if(m<r-l+1):
            m=r-l+1
            start=l
        c+=1
        l-=1
        r+=1
print(m)
print(s[start:start+m])
print(c)
        
            

    