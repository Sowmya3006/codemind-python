n,x=map(int,input().split())
rev,ab=0,0
a=str(n)
s=len(a)
for i in range(0,x):
    rev=rev*10+int(a[i])
    
    ab=ab*10+int(a[len(str(n))-x+i])
print(abs(rev-ab))    
    