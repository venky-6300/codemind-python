n=int(input())
l=list(map(int,input().split()))
a=sum(l)//len(l)
b=0
for i in l:
    if i<=a:
        b+=1
print(b)
        