'''
使用type()检查变量类型
'''
a=100
b=12.333
c=1+5j
d='hello,world'
e=True
print(type(a))	#整型	<class 'int'>
print(type(b))	#浮点	<class 'float'>
print(type(c))	#复数	<class 'complex'>
print(type(d))	#字符串	<class 'str'>
print(type(e))	#布尔	<class 'bool'>

"""
可以使用Python中内置的函数对变量类型进行转换。
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。
"""