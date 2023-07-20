def powmod(a,n,m):
    if n==0:
        return 1
    if n==1:
        return a
    p=powmod(a,n//2,m)
    if n%2==0:
        return (p*p)%m
    else:
        return (p*p*a)%m
a,n,m=map(int,input().split())
powmod(a,n,m)    
print(powmod(a,n,m))