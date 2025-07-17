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


def reverse_number(num):
    return int(str(num)[::-1])
print(reverse_number(1234))  # 输出：4321