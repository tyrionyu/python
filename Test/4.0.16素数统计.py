def is_prime(n):
    """判断一个数是否为素数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    # 只需检查到平方根范围即可
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 生成100-200之间的素数列表
primes = [num for num in range(100, 201) if is_prime(num)]

# 输出结果
print("100~200之间的素数共有{}个：".format(len(primes)))
for prime in primes:
    print(prime, end=" ")