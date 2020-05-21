for i in range(3,0,-1):
    for j in range(1,2*i):
        if j%2==0:
            print("*",end="")
        else:    
            print(i,end="")
    print("")   
