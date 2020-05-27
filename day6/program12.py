def long(a,n):  
    if n==1: 
		    return a[0] 
	  a.sort() 
	  end = min( len(a[0]), len(a[-1]) ) 
  	i = 0
	  while i < end and a[0][i] == a[-1][i]): 
		     i=i+1
    pre = a[0][0:i] 
	  return pre 

n=int(input())
l=[]
for i in range(n):
     s=str(input())
     l.append(s)     
print(long(l,n))  
