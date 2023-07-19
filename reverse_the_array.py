def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = list(map(int,input().split()))
reverseList(A, 0, len(A)-1)
print(A)
