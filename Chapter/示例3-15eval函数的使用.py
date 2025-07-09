s='3.14+3'
print(s,type(s))
x=eval(s)   #使用eval函数去掉s字个字符串左右的引号
print(x,type(x))

'''
eval函数经常与input()函数一起使用，用来获取用户输入的数值
'''
age=eval(input('请输入您的年龄：'))
print(age,type(age))

heigt=eval(input('请输入您的身高：'))
print(heigt,type(heigt))

hello='福州欢迎您'
print(hello)
print(eval('hello'))
# print(eval(hello)) #代码会出错