# 定义两个 3×3 矩阵（嵌套列表）
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# 初始化结果矩阵
result = [[0] * 3 for _ in range(3)]

# 逐元素相加
for i in range(3):
    for j in range(3):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print("结果矩阵：")
for row in result:
    print(row)