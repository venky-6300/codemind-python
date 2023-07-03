r,c=map(int,input().split())
a=[]
b=[]
for i in range(r):
    l=list(map(int,input().split()))
    a.append(sum(l))
print(max(a))
    