# 初始有序列表
sorted_list = [10, 20, 34, 56, 90]
num_to_insert = 190

# 查找插入位置
index = 0
for i in range(len(sorted_list)):
    if num_to_insert < sorted_list[i]:
        index = i  # 找到第一个比50大的元素位置
        break
else:
    index = len(sorted_list)  # 若50比所有元素大，插入末尾

# 插入元素
sorted_list.insert(index, num_to_insert)

print(sorted_list)  # 输出结果