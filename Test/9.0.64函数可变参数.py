'''请完善average()函数，使得当可变参数长度为0的时候，也能正确返回结果。'''
def average(*args):
    sum = 0
    if len(args) == 0:
        return sum
    for item in args:
        sum += item
    avg = sum / len(args)
    return avg
print(average(1,2,3,4))