""" 
# 实例变量
class Dog:
    def __init__(self,name,age):
        self.name=name  #创建和初始化实例变量name
        self.age=age    #创建和初始化实例变量age

d=Dog('球球',2) # 创建对象

print(f"我们家的狗狗叫{d.name},{d.age}岁了")    #对实例变量通过“对象实例变量”形式访问 

"""



'''
# 构造方法
class Dog:
    def __init__(self,name,age,sex='雌性'): #第一个参数必须是self(带有默认值的构造方法，能够给调用者提供多个不同版本的构造方法)
        self.name=name  #创建和初始化实例变量name
        self.age=age    #创建和初始化实例变量age
        self.sex=sex    #创建和初始化实例变量sex

d1=Dog('球球',2)    #创建对象调用构造方法，省略默认值
d2=Dog('哈哈',1,'雄性')
d3=Dog(age=5,name='拖布',sex='雄性')    #使用关键字参数调用构造方法

print(f"我们家的狗狗叫{d1.name},{d1.age}岁了")
print(f"我们家的狗狗叫{d2.name},{d2.age}岁了")
print(f"我们家的狗狗叫{d3.name},{d3.age}岁了")
'''

""" 
# 实例方法
class Dog:
    # 构造方法
    def __init__(self,name,age,sex='雌性'): #第一个参数必须是self(带有默认值的构造方法，能够给调用者提供多个不同版本的构造方法)
        self.name=name  #创建和初始化实例变量name
        self.age=age    #创建和初始化实例变量age
        self.sex=sex    #创建和初始化实例变量sex

    # 实例方法
    def run(self):  #定义实例方法，只有一个self参数
        print(f"{self.name},在跑...")

    # 实例方法
    def speak(self,sound):
        print(f"{self.name},在叫，{sound}!!!")

dog=Dog('球球',2)
dog.run()
dog.speak('旺 旺 旺')  """
'''
# 类变量
class Account:
    interest_rate=0.0568    #类变量利率iterest_rate

    def __init__(self,owner,amount):
        self.owner=owner      #创建并初始化实例变量owner
        self.amount=amount  #创建并初始化实例变量amount

account=Account('Tony',800000.0)

print(f"帐户名:{account.owner}")
print(f"帐户金额：{account.amount}")
print(f"利率:{Account.interest_rate}")

'''

'''
# 私有变量
class Account:
    __interest_rate=0.0568    #类变量利率iterest_rate

    def __init__(self,owner,amount):
        self.owner=owner      #创建并初始化实例变量owner
        self.__amount=amount  #创建并初始化实例变量amount
    
    def desc(self):
        print(f"{self.owner}金额：{self.__amount},利率:{Account.__interest_rate}")

account=Account('Tony',800000.0)
account.desc()

print(f"帐户名:{account.owner}")
# print(f"帐户金额：{account.__amount}")       # 错误发生
# print(f"利率:{Account.__interest_rate}")    # 错误发生

'''

# 私有方法
class Account:
    __interest_rate=0.0568    #类变量利率iterest_rate

    def __init__(self,owner,amount):
        self.owner=owner      #创建并初始化实例变量owner
        self.__amount=amount  #创建并初始化私有实例变量amount
    
    def __get_info(self):
        return "{self.owner}金额：{self.__amount},利率:{Account.__interest_rate}"
    def desc(self):
        print(self.__get_info)

account=Account('Tony',800000.0)
account.desc()
account.__get_info()    #发生错误