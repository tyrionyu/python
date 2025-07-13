# 全局变量 x
x = 10
def test_scope():
    # 局部变量 x，仅在函数内部有效
    x = 20
    print(f"函数内部的 x: {x}")  # 输出局部变量 x
test_scope()
print(f"函数外部的 x: {x}")  # 输出全局变量 x


# 不创建局部变量，直接修改全局变量

def modify_global():
    global x
    x = 30
    print(f"修改后的全局 x: {x}")
modify_global()
print(f"全局 x 已被修改为: {x}")
