'''请实现函数func，当参数类型为list时，返回list中所有数字类型元素的和，
当参数类型为tuple时，返回tuple中所有数字类型元素的乘积。'''
def func(param):
    if isinstance(param, list):
        result = 0
        for item in param:
            if isinstance(item, int) or isinstance(item, float):
                result += item
        return result
    elif isinstance(param, tuple):
        result = 1
        for item in param:
            if isinstance(item, int) or isinstance(item, float):
                result *= item
        return result
    return None

print(func((1,2,3,4,5)))