r,c=map(int,input().split())
b=[]
for i in range(r):
    l=list(map(int,input().split()))
    b.append(sum(l))
print(*b)