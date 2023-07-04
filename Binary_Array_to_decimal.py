n=int(input())
l=list(map(int,input().split()))
l.reverse()
a=0
for i in range(len(l)):
    a=a+((2**i)*l[i])
print(a)