n=int(input())
lst=list(map(int,input().split()))[:n]
u=set(lst)
a=list(u)
t=sorted(a,reverse=True)
if n<3:
    print(max(t))
else:
    print(t[2])