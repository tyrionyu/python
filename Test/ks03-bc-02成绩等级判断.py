'''
成绩等级判断​​

输入一个0~100的整数成绩，根据以下规则输出等级：
90分以上：A
80~89分：B
70~79分：C
60~69分：D
60分以下：F

​​要求​​：

使用 if-elif-else 结构实现
处理非法输入（如非数字、超出范围）
'''

def get_grade(score):
    try:
        score = int(score)
        if not 0 <= score <= 100:
            return "错误：成绩需在0~100之间"
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    except ValueError:
        return "错误：请输入整数"

# 测试示例
print(get_grade(89))   # 输出 B

#print(get_grade("abc")) # 输出错误提示