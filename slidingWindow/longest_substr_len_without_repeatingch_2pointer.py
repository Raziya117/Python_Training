#length of longest substring without repeating characters
s='abcbdecfbgce'
d={}
m=0
l=0
start=0
for r in range(len(s)):
    if s[r] not in d:
        d[s[r]]=r
    else:
        if d[s[r]]>=l:
            l=d[s[r]]+1
        d[s[r]]=r
    if r-l+1>m:
        m=r-l+1
        start=l
    #m=max(m,r-l+1)
print(s[start:start+m])       
print(m)

# print longest substring which must have c,d in it without repeating chatrcaters
s='abcedacefaebghd'
m='c'
n='d'
d={}
maxi=0
st=0
l=0
for r in range(len(s)):
    if s[r] not in d:
        d[s[r]]=r
    else:
        if d[s[r]]>=l:
            l=d[s[r]]+1
        d[s[r]]=r
    if r-l+1>maxi and m in d and n in d and d[m]>=l and d[n]>=l:
            maxi=r-l+1
            st=l
#     curr=s[l:r+1]
#     if m in curr and n in curr:
# #         maxi=max(maxi,r-l+1)
#         if r-l+1>maxi:
#             maxi=r-l+1
#             st=l
print(s[st:st+maxi])
print(maxi)
        
        

        
        
    
    