
'''
已知两个集合s1、s2，请判断两个集合是否有重合，如果有，请把重合的元素打印出来。

s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
'''

s1 = set([1, 2, 3, 4, 6, 8, 10])
s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
flag = s1.isdisjoint(s2)
if not flag:
    for item in s1:
        if item not in s2:
            continue
        print(item)