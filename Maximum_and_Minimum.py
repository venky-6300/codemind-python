n=int(input())
l=list(map(int,input().split()))
a=[]
for  i in l:
    if i not in a and l.count(i)==i:
        a.append(i)
if a:
    print(min(a),max(a))
else:
    print(-1)