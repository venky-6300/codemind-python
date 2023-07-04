n=int(input())
l=list(map(int,input().split()))
a=len(l)
b=0
for i in l:
    if i==1 or i==0:
        b+=1
if b==a:
    print('True')
else:
    print('False')