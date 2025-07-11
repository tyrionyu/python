'''
输入年份判断是不是闰年。
'''
years=int(input('请输入年份：'))

def is_leap_year(years):
    return (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)

if is_leap_year(years):
    print(f"{years} 是闰年。")
else:
    print(f"{years} 不是闰年。")