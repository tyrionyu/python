# 尝试定义这些变量
try:
    _name = 10       # 合法
    my_var = 20      # 合法
    print("_name 和 my_var 是合法变量名")

    # 尝试定义 3var（会报错）
    3var = 30        # SyntaxError: invalid syntax
except SyntaxError:
    print("3var 是非法变量名（不能以数字开头）")