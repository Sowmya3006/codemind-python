def isprime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True        
n=int(input())
m=int(input())
for i in range(n,m+1):
    if isprime(i)==True:
        print(i,end='
')
        