a=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(i)
b=set(c)
print(*b)