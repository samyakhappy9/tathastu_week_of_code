n1=int(input())
d=[]
for i in range(n1):
     s=str(input())
     d.append(s)
n2=int(input())
a=[]
for i in range(n2):
     s=str(input())
     a.append(s)
r=[]
se=set(a)
for i in d:
     if set(i).issubset(se):
         r.append(i)         
print(r)
