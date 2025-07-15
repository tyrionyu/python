# 冒泡法
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                # 交换元素
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

numbers = [34, 12, 89, 5]
sorted_numbers = bubble_sort(numbers.copy())
print("冒泡排序结果:", sorted_numbers)

# 选择排序法
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

numbers = [34, 12, 89, 5]
sorted_numbers = selection_sort(numbers.copy())
print("选择排序结果:", sorted_numbers)

# 插入排序法
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

numbers = [34, 12, 89, 5]
sorted_numbers = insertion_sort(numbers.copy())
print("插入排序结果:", sorted_numbers)

# 使用内置 sorted() 函数（虽然题目要求不用 sort()，但 sorted() 是不同函数）
numbers = [34, 12, 89, 5]
sorted_numbers = sorted(numbers)
print("sorted()函数结果:", sorted_numbers)

# 使用 min() 和列表操作的实现

def custom_sort(lst):
    sorted_lst = []
    while lst:
        min_val = min(lst)
        sorted_lst.append(min_val)
        lst.remove(min_val)
    return sorted_lst

numbers = [34, 12, 89, 5]
sorted_numbers = custom_sort(numbers.copy())
print("自定义排序结果:", sorted_numbers)