d = {"Alice": 45, "Bob": 60, "Candy": 75, "David": 86, "Ellena": 49}
for key in d:  # 遍历d的key
    value = d[key]
    if value > 60:
        print(key, value)

"""另外一个方法"""
for key, value in d.items():
    if value > 60:
        print(key, value)

"""同学的近三次成绩如下，请把每个同学的每次成绩依次输出。
d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}"""

d = {"Alice": [50, 61, 66], "Bob": [80, 61, 66], "Candy": [88, 75, 90]}

for key, value in d.items():
    for score in value:
        print(key, score)
