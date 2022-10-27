n=int(input())
while n>9:
    s=0
    while n!=0:
        r=n%10
        s=s+r
        n=n//10
    if s<=9:
        print(s)
        break
    else:
        n=s
        