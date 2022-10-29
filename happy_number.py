def happy(n):
    if n<9:
        return n
    else:
        s=0
        while n!=0:
            r=n%10
            s+=r*r
            n=n//10
        return s 
n=int(input())
while n>9:
    n=happy(n)
if n==1 or n==7:
    print("True")
else:
    print("False")