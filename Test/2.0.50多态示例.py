class Animal:
    def speak(self):
        raise NotImplementedError("子类必须实现此方法")

class Dog(Animal):
    def speak(self):
        return "汪汪！"

class Cat(Animal):
    def speak(self):
        return "喵喵！"

# 多态演示函数
def animal_speak(animal):
    print(animal.speak())

# 创建实例
dog = Dog()
cat = Cat()

# 调用相同的接口，产生不同的行为
animal_speak(dog)  # 输出: 汪汪！
animal_speak(cat)  # 输出: 喵喵！