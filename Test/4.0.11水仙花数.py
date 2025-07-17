for num in range(100, 1000):
    # 分解百位、十位、个位
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    
    # 判断是否满足水仙花数条件
    if num == hundreds ** 3 + tens ** 3 + units ** 3:
        print(num,end=' ')