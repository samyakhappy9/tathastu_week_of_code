n=int(input())
l=[]
k=int(input())
for i in range(n):
     x=int(input())
     l.append(x)
l.sort()
print(l[k-1])
