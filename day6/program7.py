def ack(a,b):
     if a==b:
         return b+1
     elif a>0 and b==0:
         return ack(a-1,1)
     elif a>0 and b>0:
         return ack(a-1,ack(a,b-1))
     else:
         return b+1
     
a=int(input())
b=int(input())
print(ack(a,b))  
