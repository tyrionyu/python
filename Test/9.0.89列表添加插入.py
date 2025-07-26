""" 班上已有同学['Alice', 'Bob', 'Candy', 'David', 'Ellena']，
新来报到3名同学分别是'Zero', 'Phoebe', 'Gen'，
请综合利用append()方法，insert()方法，
把三个同学的名字按首字母顺序插入到列表里去。 """

L = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
L.append('Zero')
L.insert(5,'Phoebe')
L.insert(5,'Gen')
print(L)