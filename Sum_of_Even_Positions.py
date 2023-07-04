n=int(input())
l=list(map(int,input().split()))
a=0
for i in range(len(l)):
    if i%2==0:
        a+=l[i]
print(a)