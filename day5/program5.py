def sort(List):
    odd = []
    even = []
    for x in List:
        if x % 2 == 0:
            even.append(x)
        else :
            odd.append(x)
    return sorted(odd, reverse = True) + sorted(even)

n= int(input())
l = []
for i in range(n):
    x=int(input())
    l.append(x)
print( str( sort(l) ) [1:-1] )
