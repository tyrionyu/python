text = "hello world hello"
words = text.split()  # 分割字符串：['hello', 'world', 'hello']

# 用字典统计词频
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)  # 输出：{'hello': 2, 'world': 1}