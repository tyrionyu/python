'''
由于name_set不能识别小写的名字，请改进name_set，是小写的名字也能判断在name_set里面。
names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
name_set = set(names)

'''

names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena', 'alice', 'bob', 'candy', 'david', 'ellena']
name_set = set(names)
print(name_set) # ==> set(['ellena', 'alice', 'Candy', 'Alice', 'candy', 'Ellena', 'Bob', 'David', 'bob', 'david'])