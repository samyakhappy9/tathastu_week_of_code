print()    
def fibo(n):
     if n==0:
         return 1
     if n==1:
         return 1
     x=0
     y=1
     z=x+y
     while z<=n:
         if z==n:
             return 1
         x=y
         y=z
         z=x+y
         
sum=0
n=int(input())
for i in range(n):
     x=int(input())
     if fibo(x)==1:
         sum+=x

if fibo(sum)==1:
     print("YES")
else:
     print("NO")
