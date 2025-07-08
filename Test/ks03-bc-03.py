
def grade(score):
    try:
        score=int(score)
        if not 0 <=score <=100:
            return "错误：成绩需要在0~100之间"
        if score >=90:
            return 'A'
        if score>=80:
            return 'B'
        if score>=70:
            return 'C'
        if score>=60:
            return 'D'
        else:
            return 'F'
    except ValueError :
        return "错误：请输入整数"

print(grade(99))