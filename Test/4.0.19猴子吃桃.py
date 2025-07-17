def calculate_peaches():
    peaches = 1  # 第10天的桃子数
    for _ in range(9):  # 倒推9天（第9天 → 第1天）
        peaches = (peaches + 1) * 2
    return peaches

print(f"第一天摘桃总数: {calculate_peaches()}")  # 输出：1534