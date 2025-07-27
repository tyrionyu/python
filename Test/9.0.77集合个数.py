'''已知d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}，请输出d的元素个数。'''

d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
keys = d.keys()
print(len(keys))

'''另外一个方法'''
values = d.values()
print(len(values))

'''dict提供clear()函数，可以直接清除dict中所有的元素。'''
d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
print(d) # ==> {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
d.clear()
print(d) # ==> {}

'''dict提供values()函数，可以返回dict中所有的value。'''
d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
for key in d.values():
    print(key)
# ==> [50, 61, 66]
# ==> [80, 61, 66]
# ==> [88, 75, 90]