class Car:
    def __init__(self, brand):
        self.brand = brand  # 初始化属性 brand

    def run(self):
        print(f"{self.brand}汽车正在行驶...")  # 方法功能：打印行驶信息

# 创建 Car 类的实例
my_car = Car("宝马")

# 访问属性
print(my_car.brand)  # 输出: 宝马

# 调用方法
my_car.run()  # 输出: 宝马汽车正在行驶...