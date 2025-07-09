sum=0
for i in range(1,101):
    if i%2==1:
        continue
    sum+=i
print('1~100之间的偶数之和：',sum)