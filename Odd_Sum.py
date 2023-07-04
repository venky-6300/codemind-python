n=int(input())
l=list(map(int,input().split()))
a=0
for i in range(n):
    if l[i]%2==1:
        a+=l[i]
print(a)