from itertools import permutations
import string
s=str(input())
l=permutations(s)
for i in l: 
     for j in i:
         print(j,end='')
     print('')    
     
