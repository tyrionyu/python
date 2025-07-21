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