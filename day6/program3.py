def find(l, n): 
      for i in range(n) :  
	    if l[i] <= 0 or l[i] > n: 
		     continue
      val = l[i]
      while l[val - 1] != val: 
             t = arr[val - 1] 
	     arr[val - 1] = val 
	     val = t 
             if val <= 0 or val > n: 
		      break
       for i in range(n): 
	     if l[i] != i + 1 : 
		      return i + 1 
       return n + 1
 
n=int(input())
l=[]
for i in range(n):
       x=int(input())
       l.append(x)
print(find(l,n)) 
