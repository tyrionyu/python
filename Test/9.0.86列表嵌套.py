'''有三个长方体，他们的长宽高分别是[1, 2, 3], [5, 3, 2], [7, 3, 2]，定义在数组L中，
L = [[1, 2, 3], [5, 3, 2], [7, 3, 2]]，请分别求出三个长方体的表面积。'''
L = [[1,2,3],[5,3,2],[7,3,2]]
for cube in L:
    length = cube[0]
    width = cube[1]
    height = cube[2]
    result = length * width * 2 + width * height * 2 + length * height * 2
    print(result)