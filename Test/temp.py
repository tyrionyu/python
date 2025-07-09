s='123'

try:
    num=int(s)
    print(num+10)
except ValueError:
    print('错误是一个字符串')