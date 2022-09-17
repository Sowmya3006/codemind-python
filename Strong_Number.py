def fact(n):
    return 1 if(n==0 or n==1) else n*fact(n-1)
    
a=int(input())
c=a
b=0
while a!=0:
    r=a%10
    b+=fact(r)
    a=a//10
if c==b:
    print('The number {} is a strong number'.format(c))
else:
    print('The number {} is not a strong number'.format(c))
    