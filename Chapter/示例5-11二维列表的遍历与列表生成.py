lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',104,50],
    ['深圳',121,78]
    ]
print(lst)

for row in lst:
    for item in row:
        print(item,end='\t')
    print()

#列表成成式生成一个4行5列的二维列表
lst2=[[j for j in range(5)]for i in range(4)]
print(lst2)