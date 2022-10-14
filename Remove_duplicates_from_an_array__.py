n=int(input())
l=list(map(int,input().strip().split()))[:n]
s=set(l)
lst=list(s)
for i in range(0,len(lst)):
    print(lst[i],end=" ")