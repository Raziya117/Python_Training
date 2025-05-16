#Balanced parenthesis using 
def parenthesis(n,s='',o=0,c=0):
    if len(s)==2*n:
        print(s)
        return
    if o<n:
        parenthesis(n,s+'(',o+1,c)
    if c<o:
        parenthesis(n,s+')',o,c+1)

n=3
parenthesis(n)