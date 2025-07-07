# coding=utf-8

x=float(input("请输入X:"))

y=float(input("请输入y:"))

if y!=0:
    print(f"乘积：{x*y}")
    print(f"整除：{x//y}")
    print(f"余数：{x%y}")
else:
    print("y不能等于0")
print(f"是否相等：{x==y}")