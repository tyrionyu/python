# coding=utf-8
'''函数data_of_square的时候，它接收边长一个参数，同时返回正方形的周长和面积'''
def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side

def data_of_square(side):
    C = square_perimeter(side)
    S = square_area(side)
    return C, S

print(data_of_square(10))