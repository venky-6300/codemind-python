n=int(input())
l=list(map(int,input().split()))
a=[]
for  i in l:
    if i not in a and l.count(i)==i:
        a.append(i)
if a:
    s=sum(a)/len(a)
    print('%.2f'%s)
else:
    print(-1)