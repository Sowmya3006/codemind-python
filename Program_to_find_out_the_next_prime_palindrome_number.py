def isPrime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def rev(n):
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
a=int(input()) 
a+=1
while a:
    if isPrime(a)==True and rev(a)==a:
        print(a)
        break
    else:
        a+=1