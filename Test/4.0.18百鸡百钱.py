def find_chicken():
    solutions = []
    for x in range(0, 21):          # 公鸡范围：0~20
        for y in range(0, 34):       # 母鸡范围：0~33
            z = 100 - x - y          # 计算小鸡数量
            if z % 3 == 0:           # 小鸡数量需为3的倍数
                cost = 5 * x + 3 * y + z // 3  # 总花费（整数除法）
                if cost == 100:       # 验证总花费为100元
                    solutions.append((x, y, z))
    return solutions

# 输出所有组合
combinations = find_chicken()
for x, y, z in combinations:
    print(f"公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只")