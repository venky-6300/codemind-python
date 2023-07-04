n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(l)):
    if l[i]%2==1:
        a.append(l[i])
    else:
        b.append(l[i])
print(*a,*b)