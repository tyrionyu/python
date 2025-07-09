lst=[4,65,3,78,98]
print('原列表：',lst)

#排序，默认升序
lst.sort()  #排序是在原列表的基础上进行的，不会产生新的列表对象
print('升序：',lst)

#排序，降序
lst.sort(reverse=True)
print('降序',lst)

#字符串的排序
lst2=['banana','apple','Cat','Orange']
print('原列表',lst2)
lst2.sort()
print('升序：',lst2)

#排序降序
lst2=['banana','apple','Cat','Orange']
print('原列表',lst2)
lst2.sort(reverse=True)
print('降序：',lst2)

#忽略大小写进行比较
lst2.sort(key=str.lower)
print(lst2)