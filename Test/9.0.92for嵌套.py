'''字符串s1='ABC'，字符串s2='123'，字符串s3='xyz'，请输出s1、s2、s3中所有字符的排列。'''

s1 = 'ABC'
s2 = '123'
s3 = 'xyz'
for ch1 in s1:
    for ch2 in s2:
        for ch3 in s3:
            print(ch1 + ch2 + ch3)

s_1 = 'ABC'
s_2 = '123'
for x in s_1:
    for y in s_2:
        print(x + y)