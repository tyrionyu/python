luck_num=8  #创建一个整型变量luck_num,并为其赋值为8
my_name='刘备'
print('Luck_num的数据类型时：',type(luck_num))
print(my_name,'的幸运数字是：',luck_num)

#python动态修改亦是的数据类型，通过赋值不同类型的值就可以直接修改
luck_num='你好，python'
print('Luck_num的数据类型时：',type(luck_num))

#在python中允许多个变量指向同一个值
num=number=1024
print(id(num))  #id()查看对象的内存地址 4513451632
print(id(number))   #4513451632

'''
使用变量保存数据并进行加减乘除运算
'''
a=100
b=13
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)