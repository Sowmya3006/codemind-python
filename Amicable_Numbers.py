n=int(input())
m=int(input())
c,v=0,0
for i in range(1,n):
    if n%i==0:
        c+=i
for i in range(1,m):
    if m%i==0:
        v+=i
if c==m and v==n:
    print('Amicable')
else:
    print('Not Amicable')