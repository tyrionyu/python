def my_abs(x):
    if not isinstance(x, int) or not isinstance(x, float):
        print('param type error.')
        return None
    if x >= 0:
        return x
    else:
        return -x
    
my_abs('1223')