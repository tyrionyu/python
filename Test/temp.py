"""s = "123"
try:
    num = int(s)
    print(num + 10)
except ValueError:
    print("错误是一个字符串")"""

""" def greet(name):
    print(f"Hello,{name}")
greet("Yu Zhengjia") """

""" def add(a,b=10):
    return a+b
print(add(5)) """

""" def get_sum(*num):
    return sum(num)
print(get_sum(1,2,3)) """

""" def rect_area(width,height):
    return float(width*height)

r_area=rect_area(3.3,3.3)
print(round(r_area,2)) """

""" cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car== 'bmw':
        print(car.upper())
    else:
        print(car.title()) """

""" abc = "bmw"
print(abc == "bmw")
 """
""" # 斐波那契数列：
# 前两项之和即下一项的值
a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a + b """

num=int(input('请输入您的六位中奖号码：'))

result='恭喜您中奖了！' if num==654321 else '您本期未中大奖！'
print(result)
