def ans(p,ne):
     lp=len(p)
     ln=len(ne)
     if lp==0:
         return ne[0]*ne[1]*ne[2]
     elif ln<=1:
         return p[-1]*p[-2]*p[-3]
     else:
         if lp<=2:
             return p[-1]*ne[0]*ne[1]
         else:
             return p[-1]*max(p[-2]*p[-3],ne[0]*ne[1])  

n=int(input())
p=[]
ne=[]
for i in range(n):
     x=int(input())
     if x>=0:
         p.append(x)
     else:    
         ne.append(x)
ne.sort()
p.sort()
print(ans(p,ne))
