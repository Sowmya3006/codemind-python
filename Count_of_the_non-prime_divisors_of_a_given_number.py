def prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and prime(i)==False:
        c+=1
print(c)        