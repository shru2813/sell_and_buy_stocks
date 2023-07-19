def find_second_largest(arr):
    if len(arr) < 2:
        return -1
    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return -1
    else:
        return second_largest
A = list(map(int,input().split()))
second_largest = find_second_largest(A)
print(second_largest) 