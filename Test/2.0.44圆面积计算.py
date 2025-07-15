import math

def calculate_circle_area():
    print("圆面积计算器")
    print("公式: S = π × r²")
    
    try:
        # 获取用户输入
        radius = float(input("请输入圆的半径: "))
        
        # 验证半径是否为正数
        if radius <= 0:
            print("错误：半径必须为正数！")
            return
        
        # 计算面积
        area = math.pi * (radius ** 2)
        
        # 输出结果，保留两位小数
        print(f"半径为 {radius} 的圆面积为: {area:.2f}")
        
    except ValueError:
        print("错误：请输入有效的数字！")

# 调用函数
if __name__ == "__main__":
    calculate_circle_area()