score=int(input('请输入整数成绩：'))

if not 0<score<=100:
    print('错误：成绩要这个区域1-100')
elif score>=90:
    print('a')
elif score>=80:
    print('b')
elif score>=70:
    print('b')
elif score>=60:
    print('c')
else:
    print('d')