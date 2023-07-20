def pallindrome(a,start,end):
    if  start> end:
        return True
    if a[start]!=a[end]:
        return False
    return pallindrome(a,start+1,end-1)

a=input()
start=0
end=len(a)-1
if (pallindrome(a, start, end)==True):
    print('1')
else:
    print('0')

