s=str(input())
c=0
l=[]
for i in s:
     if i not in l:
         l.append(i)
         if s.count(i)%2 ==1:
              c=c+1            
if c==0:
     print(0)
else:    
     print(c-1)
