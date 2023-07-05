n=int(input())
d=[]
c=1
b=n*n
while b:
    a=b%10
    b=b//10
    d.append(a)
if sum(d)==n:
    print('Neon Number')
else:
    print('Not Neon Number')
    
    
    