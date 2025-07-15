def simple_calculator():
    print("欢迎使用 Python 计算器")
    print("支持运算符: + (加), - (减), * (乘), / (除)")
    print("输入格式: 数字 运算符 数字 (例如: 2 + 3)")
    print("输入 'quit' 或 'q' 退出程序\n")
    
    while True:
        user_input = input("请输入表达式: ").strip()
        
        # 退出条件
        if user_input.lower() in ('quit', 'q'):
            print("感谢使用计算器，再见！")
            break
        
        # 解析输入
        parts = user_input.split()
        
        # 验证输入格式
        if len(parts) != 3:
            print("错误：请输入正确的表达式格式 (例如: 5 * 3)")
            continue
        
        num1_str, operator, num2_str = parts
        
        # 验证数字
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("错误：请输入有效的数字")
            continue
        
        # 执行计算
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("错误：除数不能为零")
                    continue
                result = num1 / num2
            else:
                print(f"错误：不支持的运算符 '{operator}'")
                continue
            
            # 显示结果（去掉不必要的 .0 显示）
            if result.is_integer():
                result = int(result)
            print(f"结果: {user_input} = {result}")
            
        except Exception as e:
            print(f"计算错误: {str(e)}")

if __name__ == "__main__":
    simple_calculator()