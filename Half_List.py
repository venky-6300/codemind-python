a=int(input())
l=list(map(int,input().split()))

b=l[len(l)//2:]
c=l[:len(l)//2]
b.reverse()
d=b+c
print(*d)