'''
内存地址验证：打印两个相同整型变量（如 x=100; y=100）的内存地址，观察是否相同。
'''
x = 100
y = 100

print("x 的内存地址:", id(x))
print("y 的内存地址:", id(y))

if id(x) == id(y):
    print("x 和 y 的内存地址相同（Python 小整数优化）")
else:
    print("x 和 y 的内存地址不同")