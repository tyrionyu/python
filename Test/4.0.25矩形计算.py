matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# 方法1：手动累加
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]  # 主对角线元素的行索引和列索引相同
    return total

print(diagonal_sum(matrix))  # 输出: 15

# 方法2：简洁写法
result = sum(matrix[i][i] for i in range(len(matrix)))
print(result)  # 输出: 15