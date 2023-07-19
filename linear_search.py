def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count
A = list(map(int,input().split()))
B = int(input())
occurrences = count_occurrences(A, B)
print(occurrences)