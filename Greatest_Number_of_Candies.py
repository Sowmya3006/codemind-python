n=int(input())
a=list(map(int,input().split()))[:n]
b=int(input())
for i in range(n):
    if a[i]+b>=max(a):
        print("True",end=' ')
    else:
        print("False",end=' ')