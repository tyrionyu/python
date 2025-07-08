'''
​​循环与跳转语句应用​​

计算1~100所有偶数的和，但跳过所有能被3整除的偶数。

​​要求​​：

1. 使用 while 或 for 循环
2. 结合 continue 跳过特定数字
3. 输出最终求和结果
'''
total = 0
for num in range(2, 101, 2):  # 遍历1~100的偶数
    if num % 3 == 0:           # 跳过能被3整除的偶数
        continue
    total += num
print(f"1~100中不被3整除的偶数和：{total}")