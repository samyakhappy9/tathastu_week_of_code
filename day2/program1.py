def prime(n):
    if n==1:
        return false
    for i in range(2,n/2 +1):
        if n%i==0:
            return false
    return true    

def odd(n):
    if n%2==1:
        return true
    else:
        return false

def even(n):
    if n%2==0:
         return true
    else:
        return false
    
def palin(n):
    s=0
    t=n
    while t>0:
        s=s*10 +t%10
        t/=10
    if s==n:
        return true
    else:
        return false
    
def arm(n):
    s=0
    t=n
    while t>0:
        r=t%10
        s+=r**3
        t/=10
    if s==n:
        return true
    else: 
        return false
    
def check():
     n=int(input())
     print("Prime:",prime(n))
     print("Odd:",odd(n))
     print("Even:",even(n))
     print("Palin:",palin(n))
     print("Arm:",arm(n))

check()
    
            
