from itertools import permutations
s=str(input())
l=permutations(s)
for i in l:
     print(''.join(i))
         
     
