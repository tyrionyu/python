#   1	1	2	3	5	8	13	21	34	55	89	​​144​

# 斐波那契数列
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# 计算第12项
print(fibonacci_iterative(12))  # 输出: 144
