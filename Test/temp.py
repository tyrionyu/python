""" s = "123"
try:
    num = int(s)
    print(num + 10)
except ValueError:
    print("错误是一个字符串") """


""" def greet(name):
    print(f"Hello,{name}")
greet("Yu Zhengjia") """

""" def add(a,b=10):
    return a+b
print(add(5)) """

""" def get_sum(*num):
    return sum(num)
print(get_sum(1,2,3)) """

def rect_area(width,height):
    return float(width*height)

r_area=rect_area(3.3,3.3)
print(round(r_area,2))