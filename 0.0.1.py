n = int(input("请输入一个正整数n: "))
sum = 0.0
for i in range(1, n+1):
    sum += 1/i
print("结果为:", round(sum, 2))