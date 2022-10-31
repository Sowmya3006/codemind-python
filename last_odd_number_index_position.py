n=int(input())
ls=list(map(int,input().split()))[:n]
for i in range(n):
    if ls[i]%2!=0:
        c=ls[i]
        a=i
print(a)        