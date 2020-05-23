def knapsack(weight, List):
    if weight == 0 or len(List) == 0:
        return 0
    if len(List) == 1:
        if List[0][0] > weight:
            return 0 
        return List[0][1]  
    if List[0][0] > weight:
        return knapsack((weight, List[1:]))
    return max(List[0][1] + knapsack(weight - List[0][0], List[1:]), knapsack(weight, List[1:]))
n =  int(input())
l = []
for i in range(n):
    w = int(input())
    value = int(input())
    l.append((w,value))
w = int(input())
print(knapsack(w, l))
