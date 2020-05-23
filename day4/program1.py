n=int(input())
l=[]
for i in range(n):
     x=int(input())
     l.append(x)
t=tuple(l)
s=int(input())
c=0
for i in t:
     if i==s:
         c+=1
print(c)        
