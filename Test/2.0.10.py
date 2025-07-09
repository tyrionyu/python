# 判断 True 是否是整数类型 int 的实例
result = isinstance(True, int)

# 打印结果
print(result)  # 输出: True

'''
# 验证布尔值的数值本质
print("True 的整数值:", int(True))     # 输出: 1
print("False 的整数值:", int(False))   # 输出: 0

# 在数学运算中的表现
print("True + True:", True + True)    # 输出: 2 (1 + 1)
print("True * 10:", True * 10)        # 输出: 10
print("False - 5:", False - 5)        # 输出: -5 (0 - 5)

# 类型层次验证
print("isinstance(False, int):", isinstance(False, int))  # 输出: True
print("type(True) is bool:", type(True) is bool)           # 输出: True
print("type(True) is int:", type(True) is int)             # 输出: False（直接类型不同）
'''