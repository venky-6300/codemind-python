n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(len(l)):
    if l[i]%2==0:
        a+=l[i]
    else:
        b+=l[i]
print(abs(a-b))