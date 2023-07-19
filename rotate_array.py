def rotate_array(A, B):
    N = len(A)
    k = B % N
    rotated = [0] * N

    for i in range(N):
        new_index = (i + k) % N
        rotated[new_index] = A[i]

    return rotated
A = list(map(int,input().split()))
B = int(input())
rotated_array = rotate_array(A, B)
print(rotated_array)