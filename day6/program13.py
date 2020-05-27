def check(arr,n):
    a=arr[0]
    b=arr[1]
    c=arr[2]
    for i in range(3,n):
        if a+b+c > 1 && a+b+c < 2:
            return true
        elif a+b+c >= 2:
            if a>b and a>c:
                 a = arr[i]
            elif b>a and b>c:
                 b = arr[i]
            elif c>a and c>b:
                 c = arr[i]
        else:
            if a<b and a<c:
                 a = arr[i]
            elif b<a and b<c:
                 b = arr[i]
            elif c<a and c<b:
                 c = arr[i]
      
     if a+b+c > 1 and a+b+c < 2:
         return true
     else: 
         return false
n=int(input())
l=[]
for i in range(n):
     x=int(input())
     l.append(x)
print(check(l,n))     
