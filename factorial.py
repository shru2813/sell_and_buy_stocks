def fact(a):
    if a==1:
        return 1
    return fact(a-1)*a
a=int(input())
print(fact(a))