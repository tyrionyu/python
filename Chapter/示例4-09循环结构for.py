#遍历字符串
for i in 'hello':
    print(i)

#range()函数，Python中的内置函数，产生一个[n,m]的整数序列，包含n,但是不包含m
for j in range(1,11):
    if j%2==0:
        print(j,'是偶数')

#计算1～10的之前的累加和
result=0
for i in range(1,11):
    result+=i
print('1~10的和是：',result)
