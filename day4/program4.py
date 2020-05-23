n=int(input())
d=dict()
for i in range(n):
     key=str(input())
     value=int(input())
     d[key]=value
d2=dict()
for key,value in d.items():
     if value not in d2.values():
         d2[key]=value
print(d2)
