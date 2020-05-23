s=str(input())
a=""
for i in s:
     if i not in a:
         a=a+i
         print(i,end='')
