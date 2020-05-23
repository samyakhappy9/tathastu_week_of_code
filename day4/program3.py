n=int(input())
d=dict()
for i in range(n):
     key=str(input())
     value=int(input())
     d[key]=value
l=list(sorted(d.values()))
print(l[-2])
