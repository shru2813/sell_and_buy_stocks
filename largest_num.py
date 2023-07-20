nums=list(map(int,input().split()))
j=[]
for num in nums:
    
    while num>0:
        d=num%10
        j.append(d)
        num = num//10
j.sort()
s=j[::-1]
p=1
sum=0
l=len(s)
while(l):
    sum=sum+s[l-1]*p
    p=p*10
    l=l-1
print(sum)