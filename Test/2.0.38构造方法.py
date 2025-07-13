""" class Car:
    def __init__(self, brand):
        self.brand = brand  # 初始化brand属性

# 测试代码
my_car = Car("Tesla")
print(my_car.brand)  # 输出: Tesla """

class Car:
    def __init__(self, brand, color="white"):  # color带默认值
        self.brand = brand
        self.color = color

# 使用示例
car1 = Car("BMW", "black")
car2 = Car("Toyota")  # 使用默认颜色white