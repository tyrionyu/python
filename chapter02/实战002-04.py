'''
从键盘获取一个4位整数，分别输出个位、十位、百位、千位上的数字。

需求: 可以使用eval()函数或者int()函数将从键盘获取的数字串转成int类型，通过整除和取余分别获取数字。
'''
num=int(input('请输入一个四位数的整数'))
print('个位上的数字为：',num%10)
print('十位上的数字为：',num//10%10)
print('百位上的数字为：',num//100%10)
print('千位上的数字为：',num//1000)