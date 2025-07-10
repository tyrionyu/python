""" year = int(input("请输入一个年份判断是不是闰年："))
def get_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if get_year(year):
    print("是闰年")
else:
    print("不是闰年") """


years = int(input("请输入一个年份断断是不是闰年："))

if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
    print(f"{years}年,是闰年")
else:
    print(f"{years}年,不是闰年")
