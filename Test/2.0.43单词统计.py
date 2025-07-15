from collections import Counter

def word_count(text):
    # 将文本分割成单词列表
    words = text.split()
    
    # 使用Counter统计单词出现次数
    word_counts = Counter(words)
    
    return word_counts

# 测试文本
sample_text = "hello world hello"

# 统计单词
result = word_count(sample_text)

# 打印结果
print("单词统计结果:")
for word, count in result.items():
    print(f"'{word}': {count}次")