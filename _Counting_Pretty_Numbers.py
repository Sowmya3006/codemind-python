t=int(input())
while(t):
    l,r=map(int,input().split())
    x=0
    for l in range(l,r+1):
       if l%10==2 or l%10==3 or l%10==9:
             x+=1
    print(x)        
    t-=1