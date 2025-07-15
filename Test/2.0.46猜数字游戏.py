import random

def enhanced_guess_game():
    print("增强版猜数字游戏")
    print("=================")
    
    # 设置难度级别
    print("\n选择难度级别:")
    print("1. 简单（1-50，最多10次尝试）")
    print("2. 中等（1-100，最多7次尝试）")
    print("3. 困难（1-200，最多5次尝试）")
    
    while True:
        level = input("请选择难度（1-3）: ")
        if level in ('1', '2', '3'):
            break
        print("请输入1、2或3！")
    
    # 根据难度设置参数
    if level == '1':
        max_num, max_attempts = 50, 10
    elif level == '2':
        max_num, max_attempts = 100, 7
    else:
        max_num, max_attempts = 200, 5
    
    secret = random.randint(1, max_num)
    attempts = 0
    
    print(f"\n我已经想好了一个1到{max_num}之间的数字，你有{max_attempts}次机会猜中它！")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\n尝试 #{attempts + 1}: "))
            
            if guess < 1 or guess > max_num:
                print(f"请输入1到{max_num}之间的数字！")
                continue
                
            attempts += 1
            
            if guess < secret:
                print("太小了！")
            elif guess > secret:
                print("太大了！")
            else:
                print(f"\n太棒了！你在{attempts}次尝试中猜中了数字{secret}！")
                return
                
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"你还剩{remaining}次尝试机会")
                
        except ValueError:
            print("请输入一个有效的整数！")
    
    print(f"\n游戏结束！你没能在{max_attempts}次内猜中数字。")
    print(f"正确答案是: {secret}")

if __name__ == "__main__":
    enhanced_guess_game()