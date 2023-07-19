def time_to_equality(A):
    max_value=A[0]
    n=len(A)
    for i in range(n):
        if A[i]>max_value:
            max_value=A[i]
    total_time=0
    for i in range(n):
        total_time+=max_value-A[i]
    return total_time
A=list(map(int,input().split()))
print(time_to_equality(A))