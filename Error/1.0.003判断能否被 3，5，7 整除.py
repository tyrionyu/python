# # B2043 判断能否被 3，5，7 整除

# ## 题目描述

# 给定一个整数 $x$，判断它能否被 $3$，$5$，$7$ 整除，并输出以下信息：

# 1、能同时被 $3,5,7$ 整除（直接输出 `3 5 7`，每个数中间一个空格）；

# 2、只能被其中两个数整除（按从小到大的顺序输出两个数，例如：`3 5` 或者 `3 7` 或者 `5 7`，中间用空格分隔）；

# 3、只能被其中一个数整除（输出这个除数）；

# 4、不能被任何数整除，输出小写字符 `n`。

# ## 输入格式

# 输入一行，包括一个整数 $x$。

# ## 输出格式

# 输出一行，按照描述要求给出整数被 $3$，$5$，$7$ 整除的情况。

# ## 输入输出样例 #1

# ### 输入 #1

# ```
# 105
# ```

# ### 输出 #1

# ```
# 3 5 7
# ```

# ## 说明/提示

# ### 数据规模与约定

# 对于全部的测试点，保证 $1 \leq x \leq 200$。

'''方案01'''
a = int(input())
divisors = []

if a % 3 == 0:
    divisors.append("3")
if a % 5 == 0:
    divisors.append("5")
if a % 7 == 0:
    divisors.append("7")

if divisors:
    print(" ".join(divisors))
else:
    print("n")

'''方案02'''
a = int(input())
result = ""

if a % 3 == 0:
    result += "3 "
if a % 5 == 0:
    result += "5 "
if a % 7 == 0:
    result += "7 "

if result:
    print(result.strip())
else:
    print("n")

'''方案03'''
def check_divisors(number):
    divisors = []
    for divisor, name in [(3, "3"), (5, "5"), (7, "7")]:
        if number % divisor == 0:
            divisors.append(name)
    return divisors

a = int(input())
result = check_divisors(a)
print(" ".join(result) if result else "n")