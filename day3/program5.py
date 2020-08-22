le1=int(input())
le2=int(input())
li1=[]
li2=[]
for i in range(le1):
     n=int(input())
     li1.append(n)

for i in range(le2):
     n=int(input())
     li2.append(n)

for i in li1:
     if i in li2:
         print(i)
         
