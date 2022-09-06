t=int(input())
while(t):
    n=int(input())
    a=1
    for i in range(n,0,-1):
        a*=i
    print(a)
    t-=1