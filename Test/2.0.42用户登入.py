def login_system():
    # 预设的用户名和密码
    correct_username = "admin"
    correct_password = "1234"
    
    # 最大尝试次数
    max_attempts = 3
    attempts = 0
    
    print("=== 用户登录系统 ===")
    
    while attempts < max_attempts:
        # 获取用户输入
        username = input("请输入用户名: ").strip()
        password = input("请输入密码: ").strip()
        
        # 验证用户名和密码
        if username == correct_username and password == correct_password:
            print("登录成功！欢迎回来，管理员！")
            return True  # 登录成功，返回True
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"用户名或密码错误！剩余尝试次数: {remaining_attempts}")
    
    # 达到最大尝试次数
    print("错误次数过多，系统已锁定！")
    return False  # 登录失败，返回False

# 调用登录系统
if __name__ == "__main__":
    login_system()