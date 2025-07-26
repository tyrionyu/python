'''
如果年龄达到18岁，则是成年人，如果年龄6岁到18岁，则是青少年，如果年龄3岁到6岁，则是小孩子，
如果年龄在3岁以下，则是婴儿，请使用if-elif-else语句实现逻辑，
如果成年，输出'adult'，
如果是青少年，输出'teenager'，
如果是小孩子，输出kid，
如果是婴儿，输出baby。
'''
age = 3

if age>=18:
    print('adult')
elif age>=6:
    print('teenager')
elif age>=3:
    print('kid')
else:
    print('baby')