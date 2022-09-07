n=int(input())
p,s=1,0
while n:
    r=n%10
    s+=r
    p*=r
    n=int(n/10)
print(p-s)    