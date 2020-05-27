import sys  
def check(l,n): 
      min= sys.maxsize 
      max= -sys.maxsize - 1
      index = -1
      for i in range(n): 
	      if l[i]< min: 
		      min=l[i] 
		      index=i
      f1 = 1
      for i in range(1,index): 
              if l[i] < l[i-1]: 
		      f1 = 0
		      break
      f2 = 1
      for i in range(index + 1,n) : 
	      if l[i] < l[i-1]: 
		      f2 = 0
		      break
      if f1+f2 ==2 and l[n-1] < l[index-1]: 
	        print("YES") 
      else: 
		print("NO") 

n=int(input())
l=[]
for i in range(n):
      x=int(input())
      l.append(x)
print(check(l, n)) 
