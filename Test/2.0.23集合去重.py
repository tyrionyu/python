# 原始列表
original_list = [1, 2, 2, 3, 3, 3]

# 使用集合去重（自动删除重复项）
unique_set = set(original_list)

# 如果结果需要是列表，转换回列表类型
unique_list = list(unique_set)

print(unique_list)  # 输出结果可能为 [1, 2, 3]（顺序可能不同）

""" from collections import OrderedDict
# 或（Python 3.7+ 可直接用原生字典）
ordered_list = list(OrderedDict.fromkeys(original_list))
# 等效简洁写法：list(dict.fromkeys(original_list))
print(ordered_list)  # 保证输出 [1, 2, 3] """