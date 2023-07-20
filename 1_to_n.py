def nums(a):
    if a>0:
        nums(a-1)
        print(a, end=' ')    
a=int(input())
nums(a)
