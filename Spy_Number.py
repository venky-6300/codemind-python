n=int(input())
b=[]
c=1
while n:
    a=n%10
    n=n//10
    b.append(a)
    c=c*a
if sum(b)==c:
    print('Spy Number')
else:
    print('Not Spy Number')
    
    