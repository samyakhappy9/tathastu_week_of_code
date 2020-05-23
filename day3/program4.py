l=[]
le=int(input())
for i in range(le):
     n=int(input())
     l.append(n)     
l2=[]
for i in l:
     if i not in l2:
         l2.append(i)
         print(i,end=' ')
    
