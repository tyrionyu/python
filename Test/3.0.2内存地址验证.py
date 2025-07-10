'''
用字典记录学生成绩：输入3个学生姓名和分数，输出最高分学生信息
'''
'''
# 创建一个空字典来存储学生信息
students = {}

# 输入3个学生的姓名和分数
for i in range(3):
    name = input(f"请输入第{i+1}个学生的姓名：")
    score = float(input(f"请输入第{i+1}个学生的分数："))
    students[name] = score

# 找出分数最高的学生
max_score = max(students.values())
top_students = [name for name, score in students.items() if score == max_score]

# 输出最高分学生信息
print("\n最高分学生信息：")
for student in top_students:
    print(f"姓名：{student}，分数：{max_score}")
'''

# 创建空字典存储学生成绩

student_scores = {}

# 输入三个学生的姓名和分数
for i in range(3):
    name = input(f"请输入第{i+1}个学生姓名：")
    score = float(input(f"请输入{name}的分数："))
    student_scores[name] = score

# 查找最高分
max_score = max(student_scores.values())

# 找到对应最高分的学生姓名
for name, score in student_scores.items():
    if score == max_score:
        max_student = name
        break  # 找到第一个最高分学生即可

# 输出结果
print("\n成绩单：", student_scores)
print(f"最高分学生：{max_student}，分数：{max_score}")