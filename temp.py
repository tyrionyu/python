# """ try语句 """
# s = "123"
# try:
#     num = int(s)
#     print(num + 10)
# except ValueError:
#     print("错误是一个字符串")

# """ 问候 """
# def greet(name):
#     print(f"Hello,{name}")
# greet("Yu Zhengjia")

# """ 求两个数的和 """
# def add(a,b=10):
#     return a+b
# print(add(5))

# """ 求和 """
# def get_sum(*num):
#     return sum(num)
# print(get_sum(1,2,3))

# """ 面积 """
# def rect_area(width,height):
#     return float(width*height)
# r_area=rect_area(3.3,3.3)
# print(round(r_area,2))

# ''' 类 '''
# cars=['audi','bmw','subaru','toyota']
# for car in cars:
#     if car== 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# abc = "bmw"
# print(abc == "bmw")

# """ 斐波那契数列 """
# # 前两项之和即下一项的值
# a, b = 0, 1
# while a < 100:
#     print(a)
#     a, b = b, a + b

# '''用户密码'''
# num=int(input('请输入您的六位中奖号码：'))
# result='恭喜您中奖了！' if num==654321 else '您本期未中大奖！'
# print(result)

# """ 自行车 """
# bikes=["giat","xds","redline"]
# print(bikes[-1],bikes[2])

# '''列表'''
# bicyles=["giat","xds","redline"]
# message=f"我的第一辆自行车是:{bicyles[0].lower()}"
# print(message)
# bicyles[1]="Merida"
# bicyles.append('Forever')
# bicyles.insert(3,"tred")
# del bicyles[4]
# print(bicyles)

# '''排序'''
# num=[9,5,2,4,8]
# # num.sort()
# # print(num)
# print(sorted(num))
# print(num)


# '''列表反转A方案'''
# friut_a=["apple","banana","mango"]
# friut_a.reverse()
# print(friut_a)     #输出 ['mango', 'banana', 'apple']


# '''列表反转B方案'''
# friut_b=["apple","banana","mango"]
# result_friut_b=friut_b[::-1]
# print(result_friut_b)   #输出 ['mango', 'banana', 'apple']

# print(len(friut_b)) 


s = "abracadabra"
count_dict = {}
for char in s:
    count_dict[char] = count_dict.get(char, 0) + 1
print(count_dict)  # 输出 {'a':5, 'b':2, 'r':2, 'c':1, 'd':1}