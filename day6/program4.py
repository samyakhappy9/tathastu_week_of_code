def find(l,c): 
    	 for i in range(c-1,0,-1): 
		        if l[i] > l[i-1]: 
			              break
			     	if i==1 and l[i] <= l[i-1]: 
		                return -1
	     x=l[i-1] 
	     sm=i 
	     for j in range(i+1,c): 
		         if l[j] > x and l[j] < l[sm]: 
			                 sm = j 
		   l[sm], l[i-1] = l[i-1], l[sm] 
	     x = 0 
	     for j in range(i): 
		           x=x*10 + l[j] 
	     l=l[i:]
       l.sort()
	     for j in range(c-i): 
		            x=x*10+l[j] 
       return x 

n=int(input())
l=map(int,n) 
print(find( l,len(l) ))
