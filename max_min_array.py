def sum_of_max_and_min(arr):
    if not arr:
        return -1
    minimum = maximum = arr[0]  
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
        elif arr[i] < minimum:
            minimum = arr[i]

    return maximum + minimum
A = list(map(int,input().split()))
result = sum_of_max_and_min(A)
print(result)