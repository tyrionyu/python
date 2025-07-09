'''
x in s

x not in s

len(s)

max(s)

min(s)

s.index(x)

s.count(x)
'''

str='HelloWorld'

print('e在HelloWorld中存在吗？',('e' in str))
print('v在HelloWorld中存在吗？',('v' in str))

#not in的使用
print('e在HelloWorld中存在吗？',('e' not in str))
print('v在HelloWorld中存在吗？',('v' not in str))

#内置函数的使用
print('len():',len(str))
print('max():',max(str))
print('min():',min(str))

#系列对像的方法，使用系列的名称，打点调用
print('str.index():',str.index('o')) #o在str中第一次出现的索引位置4
# print('str.index():',str.index('v')) #ValueError: substring not found

#统计o在字符串中出现的次数
print('str.count():',str.count('o')) 
