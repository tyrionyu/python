'''在dict中，使用keys()方法，可以返回dict的所有key，在删除某个元素时，
可以通过这个方法先判断某个元素是否存在，请改造前面的程序，
使得即使key不存在时，删除也不会抛异常。'''

d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'David': 86,
    'Ellena': 49
}
name = 'Alice'
if name in d.keys():
    d.pop(name)
else:
    print(f"{name}not in d.")
print(d)