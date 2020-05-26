import sys  
def check(arr, n): 
	  minEle = sys.maxsize 
	  maxEle = -sys.maxsize - 1
	  minIndex = -1
 
	  for i in range(n): 
		      if arr[i]< minEle: 
			        minEle = arr[i] 
			        minIndex = i
	  flag1 = 1
	  for i in range(1, minIndex): 
		      if arr[i] < arr[i - 1]: 
			        flag1 = 0
			        break
	  flag2 = 1
	  for i in range(minIndex + 1, n) : 
		      if arr[i] < arr[i - 1]: 
			        flag2 = 0
			        break
    if flag1+flag2 ==2 and arr[n-1]<arr[minIndex - 1]: 
		      print("YES") 
	  else: 
		      print("NO") 

n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
print(check(l, n)) 
