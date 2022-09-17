n=int(input())
a,b=0,1
while n!=0:
    r=n%10
    a+=r
    b*=r
    n=n//10
if a==b:
    print('Spy Number')
else:
    print('Not Spy Number')