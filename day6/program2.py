def ans(l):
	 res=[x for x in l if x==0] + [x for x in l if x==1]
	 return res
n=int(input())
l=[]
for i in range(n):
  	x=int(input())
	  l.append(x)
print(ans(l)) 
