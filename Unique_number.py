n=int(input())
s=str(n)
lst=list(s)
a=set(lst)
if len(a)==len(lst):
    print('Unique Number')
else:
    print('Not Unique Number')