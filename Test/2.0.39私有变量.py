class Car:
    def __init__(self, brand):
        self.brand = brand          # 公有属性
        self.__secret_code = "XQ9"  # 私有属性（双下划线开头）
        
    def show_secret(self):
        """类内部可访问私有属性"""
        return f"内部访问: {self.__secret_code}"

# 创建对象
my_car = Car("Tesla")

# 1. 访问公有属性
print("品牌:", my_car.brand)        # 正常访问 → Tesla

# 2. 直接访问私有属性 (将失败)
try:
    print("秘密代码:", my_car.__secret_code)  # ❌ 触发 AttributeError
except AttributeError as e:
    print(f"外部访问失败: {e}")      # 输出: 'Car' object has no attribute '__secret_code'

# 3. 通过内部方法访问
print(my_car.show_secret())         # 内部访问: XQ9

# 4. 强制访问 (不推荐!)
# Python 私有机制实际通过名称改写实现：_类名__属性名
print("强制访问:", my_car._Car__secret_code)  # → XQ9

# 注意：单下划线不是真私有（约定俗成的"保护"属性）
my_car._protect_var = "可访问但约定不直接访问"
print(my_car._protect_var)          # 虽然能访问，但不符合规范