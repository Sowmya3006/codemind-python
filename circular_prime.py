def prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
def rev(m):
    s=0
    while m!=0:
        r=m%10
        s=s*10+r
        m=m//10
    return s
    
n=int(input())
t=rev(n)
if prime(n)==True and prime(t)==True:
    print("circular prime")
elif prime(n)==True and prime(t)!=True or prime(n)!=True and prime(t)==True:
    print("prime but not a circular prime")
else:
    print("not prime")