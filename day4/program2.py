sL = int(input())
sT = int(input())
List = []
for i in range(sL):
    T = []
    for j in range(sT):
        x=int(input())
        T.append(x)
    List.append(tuple(T))
N = int(input())
List.sort(key = lambda x : x[N])
print(List)
