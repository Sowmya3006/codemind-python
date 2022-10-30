def ispalin(n):
    s,c=0,n
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    if c==s:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if ispalin(i)==True:
        print(i,end=' ')