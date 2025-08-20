k=int(input())

if k==1 or k==2:
    print(1)
else:
    a,b=1,1
    for _ in range(3,k+1):
        a,b=b,a+b
    print(b)