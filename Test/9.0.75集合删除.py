
'''
针对以下set，给定一个list，对于list里面的每个元素，如果set中包含这个元素，就将其删除，否则添加到set里面去。

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S = set([1, 3, 5, 7, 9, 11])

'''

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S = set([1, 3, 5, 7, 9])
for item in L:
    if item in S:
        S.remove(item)
    else:
        S.add(item)
print(S) # ==> set([2, 4, 6, 8, 10])