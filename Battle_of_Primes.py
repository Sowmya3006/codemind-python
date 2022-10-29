def isprime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True        
n=int(input())
m=int(input())
a=m+n
a+=1
while a:
    if isprime(a):
        print(abs(m+n-a))
        break
    else:
        a+=1