n=int(input())
l=list(map(int,input().split()))
a=sum(l)
b=a//len(l)
if b in l:
    print('True')
else:
    print('False')