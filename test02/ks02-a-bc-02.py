num=float(input("请输入浮点数："))
int_num=int(num)                                    # 截断小数部分
bool_val=bool(int_num)                              # 非零转为True，0转为False
print(f"整数部分：{int_num}，布尔数：{bool_val}")