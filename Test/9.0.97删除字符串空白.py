""" 
每个单词的首字母大写可以使用以下方法来删除空白：
lstrip()：移除左端的空白
rstrip()：移除右端的空白
strip() ：移除两端的空白 
"""

# abc=' iTruing'.lstrip()     #删除左边空白
# print(abc)

# abc='iTruing  '.rstrip()     #删除右边空白
# print(abc)

# abc='  iTruing  '.strip()     #删除左右边空白
# print(abc)

url = 'https://www.ituring.com.cn'
url = url.removeprefix('https://')  #移除特殊内容
print(url)