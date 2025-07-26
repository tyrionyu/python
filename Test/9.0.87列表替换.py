'''

班上某次考试，['Alice', 'Bob', 'Candy', 'David', 'Ellena'] 
的成绩分别是 89, 72, 88, 79, 99，请按照成绩高低，
重新排列list中同学名字的顺序。

'''

L = ['Alice','Bob','Candy','David','Ellena']
L[0] = 'Ellena'
L[1] = 'Alice'
L[2] = 'Candy'
L[3] = 'David'
L[4] = 'Bob'
print(L)