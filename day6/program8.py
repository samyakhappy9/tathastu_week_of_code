def spiral(m,n,a) : 
	  k = 0
    l = 0
  	while k < m and l < n : 
             for i in range(l, n) : 
			               print(a[k][i], end = " ") 
			       k += 1
             n-=1
             for i in range(k, m) : 
			               print(a[i][n], end = " ") 
             if k<m : 
			               for i in range(n-1, (l-1), -1) : 
				                  print(a[m-1][i], end = " ") 
	           m -= 1 
		         if l<n : 
			               for i in range(m-1, k-1, -1) : 
				                  print(a[i][l], end = " ") 
			       l += 1

r=int(input())
c=int(input())
rows, cols = (r,c) 
a=[] 
for i in range(cols): 
    col = [] 
    for j in range(rows): 
        col.append(0) 
    a.append(col)  
spiral(r,c,a) 
