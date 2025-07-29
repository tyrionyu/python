
'''请使用两种方式往空的set中添加以下名字：['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl']。'''

names = ['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl']
name_set = set()
'''第一种方法'''
# for name in names:
#     name_set.add(name)
# print(name_set)

'''第二种方法'''
name_set.update(names)
print(name_set)