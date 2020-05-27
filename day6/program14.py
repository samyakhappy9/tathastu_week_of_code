def revcol(arr,n): 
	  for i in range(n): 
		     j = 0
		     k = n-1
		     while j < k: 
			         t = arr[j][i] 
			         arr[j][i] = arr[k][i] 
			         arr[k][i] = t 
			         j += 1
			         k -= 1
	 
def transpose(arr,n): 
	    for i in range(n): 
		       for j in range(i,n): 
			           t = arr[i][j] 
			           arr[i][j] = arr[j][i] 
			           arr[j][i] = t 
            
n=int(input())
l=[]
for i in range(n):
      m=[]
      for i in range(n):
            x=int(input())
            m.append(x)
      l.append(m)      
transpose(l) 
revcol(l)  
for i in range(n): 
		   for j in range(n): 
			       print(str(arr[i][j]), end =" ") 
		   print() 
