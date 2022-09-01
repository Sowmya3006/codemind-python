l,r,k=map(int,input().split())
c=0
for l in range(l,r+1):
    if l % k ==0:
        c+=1
print(c)        