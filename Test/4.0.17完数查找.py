import math

def is_perfect(n):
    if n <= 1:
        return False
    total = 1  # 1是所有数的因子
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # 避免重复添加平方根
                total += n // i
    return total == n

perfects = [num for num in range(2, 1001) if is_perfect(num)]
print("1000以内完数:", perfects)  # 输出: [6, 28, 496]