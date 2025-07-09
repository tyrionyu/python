# 算术运算符
a = 10
b = 3
print('加法',a + b)  # 13  加法
print('减法',a - b)  # 7   减法
print('乘法',a * b)  # 30  乘法
print('除法',a / b)  # 3.3333333333333335  除法
print('取余',a % b)  # 1   取余
print('整除',a // b)  # 3  整除
print('幂运算',a ** b)  # 1000   幂运算
print('',a << 1)  # 20
print('',a >> 1)  # 5
#有优先级，幂>乘除>加减

# 比较运算符
print(a == b)  # False  等于
print(a != b)  # True   不等于
print(a > b)   # True
print(a < b)   # False

# 逻辑运算符
print(a > b and b > 0)  # True
print(a < b or b < 0)  # False
print(not (a > b))      # False

# 赋值运算符+=、-=、%=、*=、//
a += 5
print(a)  # 15
# a -= 3
# print(a)    #12


# 位运算符
print(~a)  # -16
print(a & 15)  # 9
print(a | 5)  # 15

# 成员运算符
print(2 in [1, 2, 3])  # True
print(4 not in [1, 2, 3])  # True

# 身份运算符
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)  # False，因为 x 和 y 是不同的对象
print(x is z)  # True，因为 z 引用了 x 的同一对象

# 链式赋值
a=b=c=100   #相当于a=100 b=100 c=100
print(a,b,c)

# 支持系列解包赋值
num1,num2=10,20   #相当于num1=10 num2=20
print(num1,num2)

# 交换两个变量的值
num1,num2=num2,num1 #相当于num2的值给num1,将num1的值给num2
print(num1,num2)