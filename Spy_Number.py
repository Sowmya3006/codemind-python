n=int(input())
a,b=0,1
while n:
    r=n%10
    a+=r
    b*=r
    n=int(n/10)
if(a==b):
    print('Spy Number')
else:
    print('Not Spy Number')