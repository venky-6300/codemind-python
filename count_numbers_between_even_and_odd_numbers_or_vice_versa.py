n=int(input())
l=list(map(int,input().split()))
a=0
for i in range(n-2):
    if l[i]%2==0 and l[i+2]%2==1 or l[i]%2==1 and l[i+2]%2==0:
        a+=1
print(a)