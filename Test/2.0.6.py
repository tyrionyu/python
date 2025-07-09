'''
try:
    # 尝试执行的代码
    # 可能引发异常的语句
except [异常类型]:
    # 发生异常时的处理代码
else:
    # 没有发生异常时执行的代码
finally:
    # 无论是否发生异常都会执行的代码

str='123'
result=int(str)+10

print(result)

# float()函数

num = float("12.3")  # 转换为浮点数 12.3


# int()函数

int("123")  # 正确 → 123
int("12.3") # 报错（不能直接转浮点字符串）
int("abc")  # 报错（不是数字）

# try 用法
try:
    # 可能引发异常的代码
except 异常类型:
    # 异常发生时的处理代码


# 处理 ValueError 和 TypeError 
try:
    num = int("123")
    result = num + "abc"  # 这里会报 TypeError
except ValueError:
    print("输入的不是有效数字！")
except TypeError:
    print("类型错误，不能相加！")
'''

s = "123"
try:
    num = int(s)
    print(num + 10)
except ValueError:
    print("字符串不是有效的数字！")
