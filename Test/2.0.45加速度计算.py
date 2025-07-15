def calculate_acceleration():
    print("加速度计算器")
    print("公式: a = (v - u) / t")
    print("其中:")
    print("u = 初速度")
    print("v = 末速度")
    print("t = 时间间隔")
    
    try:
        # 获取用户输入
        u = float(input("请输入初速度(u): "))
        v = float(input("请输入末速度(v): "))
        t = float(input("请输入时间间隔(t): "))
        
        # 验证时间间隔是否为正数
        if t <= 0:
            print("错误：时间间隔必须为正数！")
            return
        
        # 计算加速度
        a = (v - u) / t
        
        # 输出结果，保留两位小数
        print(f"\n计算结果:")
        print(f"初速度(u) = {u}")
        print(f"末速度(v) = {v}")
        print(f"时间间隔(t) = {t}")
        print(f"加速度(a) = {a:.2f}")
        
    except ValueError:
        print("错误：请输入有效的数字！")

# 调用函数
if __name__ == "__main__":
    calculate_acceleration()