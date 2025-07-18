""" num = 1234
def abc():
    s = num // 1000
    h = (num // 100) % 10
    t = (num // 10) % 10
    u = num % 10
    return u * 1000 + t * 100 + h * 10 + s
result = abc()
print(result)
print(type(result)) """


""" 使用字符串反转 """
def reverse_number(num):
    return int(str(num)[::-1])
print(reverse_number(1234))  # 输出：4321

""" 使用数学运算 """
num = int(input("请输入一个整数："))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print(reversed_num)

""" 使用递归 """
def reverse_number(n, reversed_n=0):
    if n == 0:
        return reversed_n
    return reverse_number(n // 10, reversed_n * 10 + n % 10)

num = int(input("请输入一个整数："))
print(reverse_number(num))

""" 下面是Python中反转整数的实现代码,通过字符串反转实现,并处理了负数、前导零及空输入等情况： """
s_input = input().strip()
if not s_input:
    print(0)
else:
    try:
        num = int(s_input)
        s = str(num)
        if s[0] == '-':
            # 负数：反转负号后的部分并重新组合
            reversed_str = '-' + s[1:][::-1]
        else:
            reversed_str = s[::-1]  # 正数直接反转
        result = int(reversed_str)  # 转换为整数自动处理前导零
        print(result)
    except Exception:
        print(0)  # 输入非法时输出0