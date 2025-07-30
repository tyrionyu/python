def data_of_square(side):
    C = 4 * side
    S = side * side
    return C, S

C, S = data_of_square(16)
result = data_of_square(16)
C = result[0]
S = result[1]
print(type(result))
'''
注意打印的result，其实它是tuple类型，如果我们需要取出结果中的周长或者面积，
使用对应位置的下标就可以获得对应的结果。
'''
print(f'周长 = {C}') # ==> 周长 = 64
print(f'面积 = {S}') # ==> 面积 = 256