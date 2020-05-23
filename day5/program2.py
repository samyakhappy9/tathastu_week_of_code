def replace(List):
    for i in range(size-1):
        List[i] = max(List[i+1:])
    return List
    
n = int(input())
l = []
for i in range(n):
    x=int(input())
    l.append(x)
print(replace(l))
