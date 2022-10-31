n=int(input())
a=list(map(int,input().split()))[:n]
c=[]
for i in range(n):
    c.append(a[i]*a[i])
b=sorted(c)
for i in range(n):
    print(b[i],end=' ')