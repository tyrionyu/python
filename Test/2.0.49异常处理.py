try:
    number = int("abc")
    print("转换成功:", number)
except ValueError:
    print("错误：无法将字符串 'abc' 转换为整数")