def Sum(List,size,sum):
     sl=[]
     if size==1:
         for x in List:
             sl.append(sum+x)
         return sl    
     L2=list(List)
     for x in List:
         L2.remove(x)
         sl.extend(Sum(L2,size-1,sum+x))
     return sl    
size=int(input())

List=[]
for i in range(size):
     n=int(input())
     List.append(n)
     
sul=list(List)
for i in range(2,size+1):
     sul.extend(Sum(List,i,0))
num=1    
for i in sul:
     if num not in sul:
         print(num)
         break
     else:    
         num+=1
         
