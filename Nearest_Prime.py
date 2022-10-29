def isPrime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def nearPrime(n,x):
    while isPrime(n)==False:
        n+=x
    return n
t=int(input())
while t:
    n=int(input())
    an=nearPrime(n,1)
    bn=nearPrime(n,-1)
    if abs(an-n)>abs(bn-n):
        print(bn)
    elif abs(an-n)<abs(bn-n):
        print(an)
    else:
        print(min(an,bn))
    t-=1    