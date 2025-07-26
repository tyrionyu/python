'''

L = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']，
由于Candy，David依次转学，某同学写出以下代码，请判断以下代码是否可以正常运行？
如果不可以，为什么？请帮忙修正。

L = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
L.pop(2)
L.pop(3)
print(L)

'''

L = ['Alice','Bob','Candy','David','Ellena']
L.pop(2)
L.pop(2)
print(L)