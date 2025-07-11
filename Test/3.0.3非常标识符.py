'''
python 输入字符串，统计数字字符个数（如"a1b23"输出3）
'''
s = input("请输入一个字符串：")
count = 0

for char in s:
    if char.isdigit():
        count += 1

print("数字字符的个数是：", count)