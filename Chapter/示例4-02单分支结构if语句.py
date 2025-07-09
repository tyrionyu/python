num=input('请输入您的6位中奖号码：')
if num==987654:
    print('恭喜您，您中奖了！')

if num!=987654:
    print('您未中本期大奖')


'''
输入一个值判断是不是偶数
'''
x=int(input('请输入一个数字判断是否是偶数：'))
if x%2:
    print(x,'奇数')

if not x%2:
    print(x,'偶数')

'''
输入一个值判断是不是空字符串
'''
y=input('请输入一个字符串判断是否是空字符串：')

if y:   #在python中一切皆对象，每个对象都有一个布尔值，而非空字符串的布尔值为True,空字符串的布尔值为False
    print('y是一个非空字符串')

if not y:   # 空字符串的布尔值为False，取反,not False的结果为True
    print('y是一个字符串')

print('使用if语句时，如果语句块只有一句代码，可以将语句块直接写在冒号的后面')

a=10
b=5
if a>b:max=a    #语句快只有一句，赋最大值
print('a和b的最大值是：',max)