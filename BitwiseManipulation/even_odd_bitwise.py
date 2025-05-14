#EVEN OR ODD CHECKING WITHOUT %
#USING & OPERATOR 
n=int(input())
if n&1==0:
    print('even')
else:
    print('odd')

# OR ---> O(1)
#USING XOR
n=int(input())
if n^1==n+1:
    print('even')
else:
    print('odd')
    
#USING XOR
n=int(input())
if n^(n-1)!=1:
    print('even')
else:
    print('odd')



