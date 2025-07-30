"""定义一个函数sub_sum()，这个函数接收一个列表作为参数，
函数返回列表所有奇数项的和以及所有偶数项的和。"""


def sub_sum(lst):
    odd_sum = 0
    even_sum = 0
    for index, item in enumerate(lst):
        if index % 2 == 0:  # 奇数索引项
            odd_sum += item
        else:  # 偶数索引项
            even_sum += item
    return odd_sum, even_sum


odd_total, even_total = sub_sum([1, 2, 3])

print(f"偶数和是：{odd_total}，奇数和是：{even_total}")
