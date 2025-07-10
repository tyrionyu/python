score=int(input('请输入成绩：'))

if not 0<=score<=100:
    print('成绩有误！')
elif score>=90:
    print('a')
elif score>=80:
    print('b')
elif score>=70:
    print('c')
else:
    print('d')