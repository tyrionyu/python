x=10
y=3
z=x/y   #在执行除法运算的时候，将运算的结果赋值给Z
print(z,type(z))

'''
float类型转换成int类型，只保留整数部分
'''
print('float类型转换成int类型',int(3.14))
print('float类型转换成int类型',int(3.9))
print('float类型转换成int类型',int(-3.14))
print('float类型转换成int类型',int(-3.9))

'''
将int类型转换成float类型
'''
print('将int类型转换float类型：',float(10))

'''
将str类型转换成int类型
'''
print(int('100')+int('200'))

#chr()ord()是一对
print(ord('俞'))
print(chr(20446))

# 进制之间的转换,转换成后是字符串
print('十进制转成十六进制：',hex(20446))
print('十进制转成八进制：',oct(20446))
print('十进制转成二进制：',bin(20446))