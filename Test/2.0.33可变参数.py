def sum_all(*args):
    """计算任意个数字的和"""
    total = 0
    for num in args:
        total += num
    return total

# 示例调用
print(sum_all(1, 2, 3))        # 输出: 6
print(sum_all(10, 20, 30, 40)) # 输出: 100
print(sum_all(5))              # 输出: 5
print(sum_all())               # 输出: 0