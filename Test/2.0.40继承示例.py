class Car:
    """父类：汽车基类"""
    def __init__(self, brand):
        self.brand = brand  # 公共属性
    
    def display_info(self):
        """显示基本信息"""
        print(f"品牌: {self.brand}")

# 创建子类 ElectricCar
class ElectricCar(Car):
    """子类：电动汽车"""
    def __init__(self, brand, battery_capacity):
        # 调用父类构造方法初始化公共属性
        super().__init__(brand)  
        # 新增子类特有属性
        self.battery = battery_capacity  # 电池容量 (单位: kWh)
    
    def display_info(self):
        """重写父类方法：扩展显示电池信息"""
        super().display_info()  # 调用父类方法
        print(f"电池容量: {self.battery}kWh")
    
    def charge(self):
        """子类新增方法：充电行为"""
        print(f"{self.brand}电动车正在充电中...")

# 创建子类实例
tesla = ElectricCar("Tesla", 75)

# 访问继承的父类属性
print(f"车辆品牌: {tesla.brand}")       # Tesla

# 访问子类新增属性
print(f"电池容量: {tesla.battery}kWh") # 75kWh

# 调用重写的方法
tesla.display_info()
# 输出:
# 品牌: Tesla
# 电池容量: 75kWh

# 调用子类新增方法
tesla.charge()  # Tesla电动车正在充电中...

# 继承关系验证
print(issubclass(ElectricCar, Car))     # True
print(isinstance(tesla, Car))           # True
print(isinstance(tesla, ElectricCar))   # True