'''变量交换'''
a=10
b=20
a,b=b,a
print(a,b)

'''条件赋值'''
score=85
result="及格" if score>60 else "不及格"
print(result)

'''创建列表'''
squares=[i*i for i in range(5)]
print(squares)

'''拼接字符串'''
words=["Hello","Python","World"]
word_list=" ".join(words)
print(word_list)

'''获取索引'''
items=["A","B","C"]
for index,item in enumerate(items):
    print(index,item)

'''字符串反转'''
text_s='hello'
print(text_s[::-1]) #输出：olleh

'''字符串拼接'''
words=['python','is','awesome']
print(' '.join(words))

'''字符串格式化'''
name='Alice'
age=25
print(f"{name} is {age} years old.")

'''分割字符串'''
text_split='apple,banana,cherry'
print(text_split(','))

'''替换字符串内容'''
text_abc='I like Java'
print(text_abc.replace('java','python'))