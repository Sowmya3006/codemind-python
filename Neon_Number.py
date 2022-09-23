n=int(input())
p=n*n
c=0
while p>0:
    r=p%10
    c+=r
    p=p//10
if c==n:
    print('Neon Number')
else:
    print('Not Neon Number')