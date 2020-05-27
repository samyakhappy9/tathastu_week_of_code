def ans(l,n):
    if n==1:
         return l[0]
    if n==2:
         if l[0]<l[1]:
              return l[0]
         else:
              return -1
    a=l[::]
    a.sort()
    if l[0]==a[0] and a[0]<a[1]:
         return a[0]
    for i in range(1,n-1):
         f=0
         g=0
         s=l[i:]
         s.sort()
         if l[i]==s[0] and s[0]<s[1]:
             f=1
         t=l[:i+1]
         t.sort()
         if t[-1]==l[i] and t[-1]>t[-2]:
              g=1
         if f+g==2:
              return l[i]
     if a[-1]==l[-1] and a[-1]>a[-2]:
         return l[-1] 
     return -1
     
n=int(input())
l=[]
for i in range(n):
     x=int(input())
     l.append(x)
print(ans(l,n))     
     
        
