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
    '''用于在遍历序列（如列表、元组、字符串）时，同时获取元素的索引和值​​。'''
    '''enumerate(iterable, start=0)
         ​​iterable​​：需要遍历的可迭代对象（如列表、字符串等）。
         ​​start​​（可选）：计数起始值，默认为 0。'''
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
print(text_split.split(','))    # 输出：['apple', 'banana', 'cherry']

'''替换字符串内容'''
text_abc='I like Java'
print(text_abc.replace('Java','Python'))    # 输出：I like Python，注意：这个方法区分大小写

'''提示词可能超过一行'''
prompt='请输入名称，这一行太长了，放不下'
prompt+='\n麻烦请输入名称：'
print(prompt)