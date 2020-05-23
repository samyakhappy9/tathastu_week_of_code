def Value(List):
    if len(List) == 2:
        return max(List)
    if len(List) == 1:
        return List[0]
    if len(List) == 3:
        return max(List[1], List[0] + Value(List[2]))
    return max(List[1] + Value(List[3:]), List[0] + Value(List[2:]))
    
n = int(input())
l = []
for i in range(n):
    x=int(input())
    l.append(x)
print(Value(l))
