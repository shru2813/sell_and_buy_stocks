lst = list(map(int, input().split()))
start = int(input())
end = int(input())
def reverse_Range(lst, i, j):
    
    while(i < j):
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        i += 1
        j -= 1
    return lst
print(reverse_Range([1, 2, 3, 4], 2, 3))
print(reverse_Range([2, 5, 6], 0, 2))
print(reverse_Range(lst, start, end))