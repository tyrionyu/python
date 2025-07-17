num = int(input("请输入一个年份数据："))

if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
    print(f"{num},是一个闰年")
else:
    print(f"{num},是一个平年")