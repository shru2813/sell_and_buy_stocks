a= list(map(int,input().split()))
de=[]
for i in range(0,len(a)):
    for j in range(1,len(a)):
        if a[i]<a[j]:
            d=a[j]-a[i]
            de.append(d)
        elif a[i]>a[j]:
            d=a[i]-a[j]
            de.append(d)
result=max(de)
print(result)