num = 8
lsb = num & 1  # 获取最低有效位

# 输出结果
print(f"数字 {num} 的二进制: {bin(num)}")  # bin() 显示二进制形式

print(f"最低有效位 (LSB): {lsb}")

print(f"结论: 数字 {num} 是{'奇数' if lsb else '偶数'}")