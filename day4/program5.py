n=int(input())
l=[]
for i in range(n):
     s=str(input())
     l.append(s)
name=l[0]
max=0
for i in l:
     if l.count(i)>=max:
         max=l.count(i)
         if i<=name:
             name=i
             
print(smname)
