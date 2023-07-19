n = int(input())
lst = []
for i in range(0, n):
    l = list(map(int, input().split()))
    lst.append(l)
r = [0] * 5
print(r)
def anti_Diagonal(lst):
    N = len(lst)
    result = []
    for c in range(0, N):
        j = c
        i = 0
        r = [0] * N
        while(i < N and j >= 0):
             r[i] = lst[i][j]
             i += 1
             j -= 1
        result.append(r)
    for c in range(1, N):
        j = N - 1
        i = c
        r = [0] * len(lst)
        while(i < len(lst) and j >= 0):
             r[j] = lst[i][j]
             i += 1
             j -= 1
        result.append(r[::-1])
    return result
print(anti_Diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(anti_Diagonal([[1, 2], [3, 4]]))
print(anti_Diagonal(lst))
