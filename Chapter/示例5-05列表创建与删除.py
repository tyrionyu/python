#直接用[]创建列表
lst=['Hello World',98,100.5]
print(lst)

#可以用内置了函数list()创建列表
lst2=list('Hello World')
lst3=list(range(1,10,2))#从1开始到10结束，步长为2，不包含10
print(lst2)
print(lst3)

#列表序列中的一种，对序列的只剩符，运算符，函数均可以使用
print(lst+lst2+lst3) #序列的相加操作
print(lst3*3) #序列的相乘操作
print(len(lst3))
print(max(lst3))
print(min(lst3))

print(lst3.count('1'))#编辑'1'的个数
print(lst2.index('W'))#w在列表2中第一次出现的位置

#列表的删除
lst4=[10,20,30]
print(lst4)

#删除列表
del lst4
# print(lst4)