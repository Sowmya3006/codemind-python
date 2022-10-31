n=int(input())
a=list(map(int,input().split()))[:n]
b=list(map(int,input().split()))[:n]
c=[]
for i in range(n):
   print(a[i]+b[i],end=" ")