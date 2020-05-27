l=[]
n=int(input())
for i in range(n):
     a=[]
     for j in range(n):
         b=int(input())
         a.append(b)
     a.sort()
     for k in a:
         l.append(k)
l.sort()
print(l)
