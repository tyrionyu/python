# coding=utf-8
'''请分别使用循环和递归的形式定义函数，求出1~100的和。'''

# 循环
def my_sumA(n):
    sum = 0
    index = 1
    while index <= n:
        sum += index
        index += 1
    return sum

# 递归
def my_sumB(n):
    sum = 0
    if n == 1:
        sum = n
    else:
        sum = n + my_sumB(n - 1)
    return sum