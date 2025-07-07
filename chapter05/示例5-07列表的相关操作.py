lst=['Hello','World','python']

print('原列表:',lst,id(lst))

#增加元素的操作
lst.append('SQL')
print('增加元素之后:',lst,id(lst))

#列表元素的删除
lst.remove('World')
print('删除元素之后的列表',lst,id(lst))

#使用insert(index,x)在指定的index位置上插入元素X
lst.insert(1,'Excel')
print(lst)

#使用pop(inde)根据索引元素取出，然后再删除
print(lst.pop(1))
print(lst)

# #清除列表中的所有的元素clear()
# lst.clear()
# print(lst,id(lst))

#列表的反向
lst.reverse()
print(lst)

#表表的拷贝，将产生一个新的列表对象
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#列表元素的修改操作
#根据索引进行修改元素
lst[1]='MySQL'
print(lst)

#